import requests

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

        if 'error' in result:
            raise Error(result['error'])
        if 'warnings' in result:
            print(result['warnings'])
        if 'query' in result:
            yield result['query']
        if 'continue' not in result:
            break
        lastContinue = result['continue']

# Converts a page model into our internal model
def makePageModel(pageJson):
    print("stuff")

if __name__ == '__main__':
    print("[")
    for result in query({'generator': 'allpages', 'formatversion': '2', 'prop': 'revisions', 'rvprop':'content'}):
        print(result)
    print("]")
