#!/usr/bin/env python
from flask import Flask, render_template
import mwclient
import requests

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

for result in query({'generator': 'allpages', 'formatversion': '2', 'prop': 'revisions', 'rvprop':'content'}):
    with open('test.txt', 'w') as f:
        print(result, file=f)



# app = Flask(__name__)
# app.config.from_envvar('CREATE_CFG')


# @app.route('/')

# def index():
#     site = mwclient.Site('en.wikipedia.org')
#     return render_template('index.html', site=mwclient.Site('http://www.copyrightevidence.org/evidence-wiki', path='/'))


# if __name__ == '__main__':

#     app.run(host='0.0.0.0', port=app.config['PORT'])