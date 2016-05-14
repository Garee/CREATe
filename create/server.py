#!/usr/bin/env python

from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config.from_envvar('CREATE_CFG')


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
