#!/usr/bin/python3
"""
index module

Methods
-------
status_route : None
    Return API status

stats_route : None
    Return JSON file with <class>:<num_instances>>
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', methods=['GET'])
def status_route():
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
def stats_route():
    """Return a json with all objects in storage"""

    return jsonify({
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User),
        })
