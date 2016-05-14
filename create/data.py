import sqlite3
import json

conn = sqlite3.connect('database.sqlite')
c = conn.cursor()
conn.row_factory = sqlite3.Row

data = conn.execute('''SELECT p.page_id AS "page_id",
p.page_title,
r.rev_text_id AS "revision_id",
t.old_id AS "text_id",
t.old_text
FROM
page p
    INNER JOIN revision r
        ON p.page_id = r.rev_page
    INNER JOIN text t
        ON r.rev_text_id = t.old_id'''
)

# keys = {0: 'page_id', 1: 'page_title', 2: 'revison_id', 3:}

def buildModel():
    pageModels = []

    for row in data:

        pageId = row[0]
        pageTitle = row[1]
        old = row[4]

        lines = old.split("\n")

        attributes = []
        for line in lines:
            if "=" in line and line.startswith('|'):
                keyValStr = line.replace("|","")

                #print (keyValStr)
                keyVal = keyValStr.split("=")
                key = keyVal[0]

                key = key.replace("?","")

                if '{' in key:
                    continue


                value = keyVal[1]

                attributes.append({'key' : key, 'value': value})

        pageModel = {
            'pageId' : pageId,
            'title' : pageTitle,
            'text' : old,
            'attributes': attributes
        }

        if attributes:
            pageModels.append(pageModel)

    return pageModels

pageModels = buildModel()

print(json.dumps(pageModels))
