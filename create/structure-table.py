import sqlite3
conn = sqlite3.connect('database.sqlite')

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

print(data)


