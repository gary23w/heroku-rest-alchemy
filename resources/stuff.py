from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.stuff import StuffModel

class Stuff(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('stuff',
        type=str,
        required=True,
        help="Put Stuff Here"
    )

    @jwt_required()
    def get(self, name):
        stuff = StuffModel.find_by_name(name)
        if stuff:
            return stuff.json()
        return {'message': 'STUFF not found'}, 404

    def post(self, name):
        if StuffModel.find_by_name(name):
            return {'message': "SOME STUFF with name '{}' already exists.".format(name)}, 400

        data = Stuff.parser.parse_args()

        stuff = StuffModel(name, **data)

        try:
            stuff.save_to_db()
        except:
            return {"message": "An error occurred inserting STUFF"}, 500

        return item.json(), 201

    def delete(self, name):
        stuff = StuffModel.find_by_name(name)
        if stuff:
            stuff.delete_from_db()

        return {'message': 'STUFF deleted'}


class StuffList(Resource):
    def get(self):
        return {'stuff': [x.json() for x in StuffModel.query.all()]}
