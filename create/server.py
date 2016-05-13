#!/usr/bin/env python

from flask import Flask, render_template


app = Flask(__name__)
app.config.from_envvar('CREATE_CFG')


@app.route('/')
def index():
    images = [
        'cloud.png',
        'trulia.png',
        'chord.png',
        'veroni.png',
        'bundling.png',
        'bubble.png'
    ]
    return render_template('index.html', images=images)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config['PORT'])
