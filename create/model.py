import requests
import json

model = []

def query(request):
    request['action'] = 'query'
    request['format'] = 'json'
    lastContinue = {'continue': ''}
    while True:
        # Clone original request
        req = request.copy()
        # Modify it with the values returned in the 'continue' section of the last result.
        req.update(lastContinue)
        # Call API
        result = requests.get('http://www.copyrightevidence.org/evidence-wiki/api.php', params=req).json()
        result = json.dumps(result)
        yield result

# Converts a page model into our internal model
def makePageModel(pageJson):
    print("stuff")

if __name__ == '__main__':
    print("[")
    for result in query({'generator': 'allpages', 'formatversion': '2', 'prop': 'revisions', 'rvprop':'content'}):
        print(result)
        print(",")
    print("]")
