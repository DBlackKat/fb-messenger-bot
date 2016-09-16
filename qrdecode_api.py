#!flask/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import re
import string
import qrtools,urllib,os
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/DORM/api/v1.0/120/new',methods = ['POST'])
def create_item():
    if not request.json or not 'url' in request.json:
        abort(400)
    image = urllib.URLopner()
    image.retrive(request.json['url'],"/home/ks2/image/url.jpg")
    qr = qrtools.QR()
    result = qr.decode("/home/ks2/image/url.jpg")
    try:
        os.remove("/home/ks2/image/url.jpg")
    except OSError:
        pass

    if result:
        return jsonify({'value':str(qr.data)}), 201
    else:
        return jsonify({'value':'404'}), 201

if __name__ == '__main__':
  app.run(debug=True)#(host='0.0.0.0', port=8000)
