import requests
import json
import time

model = []

# A generator that returns all the pages from the wiki
def allPagesGenerator(request):
    request['action'] = 'query'
    request['format'] = 'json'
    lastContinue = {'continue': ''}

    # Time it out because i have no idea how to use the API properly
    timeStart = time.time()
    while time.time() < timeStart + 120 :
        # Clone original request
        req = request.copy()
        # Modify it with the values returned in the 'continue' section of the last result.
        req.update(lastContinue)
        # Call API
        resultPy = requests.get('http://www.copyrightevidence.org/evidence-wiki/api.php', params=req).json()

        yield resultPy

# Converts a page model into our internal model
def makePageModel(pageJson):
    print("stuff")

if __name__ == '__main__':
    results = []
    for result in allPagesGenerator({'generator': 'allpages', 'formatversion': '2', 'prop': 'revisions', 'rvprop':'content'}):
        results.append(result)

    asJson = json.dumps(results)

    print(asJson)
