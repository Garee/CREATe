#!/usr/bin/env python

from flask import Flask, render_template, jsonify, request

import json

app = Flask(__name__)
app.config.from_envvar('CREATE_CFG')

@app.route('/pages')
def pages():
    with open('all_data.txt') as data_file:
        pages = json.load(data_file)

        key = request.args.get('key')

        results = []
        for page in pages:
            attrs = page['attributes']

            for attr in attrs:
                if attr['key'] == key:
                    result = {
                        'title' : page['title'],
                        'pageId' : page['pageId'],
                        key: attr['value']
                    }
                    results.append(result)
        return jsonify({
            "results": results
        })

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cloud')
def cloud():
    return render_template('cloud.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])
