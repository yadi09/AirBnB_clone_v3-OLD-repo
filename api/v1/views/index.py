#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    status = {"status": "OK"}
    return jsonify(status)
