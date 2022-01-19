from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        item = StoreModel.find_by_name(name)
        if item:
            return item.json()
        return {'Item': "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name {} already exists ".format(name)}, 400

        item = StoreModel(name)
        try:
            item.save_to_db()
        except:
            return {'message': "An error occurred while creating the store."}, 500
        return item.json(), 201

    def delete(self, name):
        item = StoreModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'items': [item.json() for item in StoreModel.query.all()]}