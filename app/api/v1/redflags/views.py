from flask_restful import Resource
from flask import jsonify, make_response, request, abort

import datetime

incidents = []


class RedFlags(Resource):
    """docstring for RedFlags"""
    
    def __init__(self):
        self.db = incidents
        if len(self.db) == 0:
            self.id = 1
        else:
            self.id = self.db[-1]['id'] + 1    

    def get(self):
        """method to get all redflags"""

        return make_response(jsonify({
            "status" : 200,
            "data" : self.db
        }), 200) 
       
    
    def post(self):
        """method to post a redflag"""
        
        data = {
            'id' : self.id,
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json['createdBy'],
            'type' : 'red-flags',
            'location' : request.json.get('location', ""),
            'status' : "draft",
            'images' : request.json.get('images', ""),
            'videos' : request.json.get('videos', ""),
            'title' : request.json['title'],
            'comment' : request.json.get('comment', "")
        }
        self.db.append(data)
        
        success_message = {
            "id" : self.id,
            "message" : "Created red-flag record"
        }

        return make_response(jsonify({
            "status" : 201,
            "data" : success_message
        }), 201)
    
