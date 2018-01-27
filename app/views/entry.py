from flask import Flask, request
from flask_restful import Resource, Api
from app import api

entrys = {10: 'hello'}


#@api.resource('/entry/<int:entry_id>')
class EntryView(Resource):

    def get(self, entry_id):
        print(entry_id)
        return {entry_id: entrys[entry_id]}

    def put(self, id):
        entrys[id] = request.form['data']
        return {id: entrys[id]}


