#!/usr/bin/env python

from flask import Flask, render_template, jsonify, request

import json

app = Flask(__name__)
app.config.from_envvar('CREATE_CFG')

@app.route('/pages')
def pages():
    with open('new_all_data.txt') as data_file:
        pages = json.load(data_file)

        key = request.args.get('key')
        limit = request.args.get('limit');
        if not limit and not key:
            return jsonify({
                "results": pages
            })
        elif key and not limit:
            limit = len(pages)
        else:
            limit = int(limit)

        results = []
        count = 0

        if key:

            for page in pages:
                if limit == count:
                    break
                attrs = page['attributes']
                print(attrs)

                for attr in attrs:
                    if attr['key'] == key:
                        result = {
                            'title' : page['title'],
                            'pageId' : page['pageId'],
                            'value': attr['value']
                        }

                        results.append(result)
                        count += 1
                        break
        else:
            while count <= limit:
                results.append(pages[count])
                count += 1


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

@app.route('/pages/keys')
def keys():

    with open('new_all_data.txt') as data_file:
        pages = json.load(data_file)

        attributes = []
        for page in pages:
            attrs = page['attributes']

            for attr in attrs:
                print (attr['key'])
                attributes.append(attr['key'])

        uniqueAttributes = list(set(attributes))

        print(uniqueAttributes)

        return jsonify({'attributes': uniqueAttributes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])
