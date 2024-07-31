from flask import Flask
from flask_restful import Api, Resource, reqparse

from get_response import get_answer

app = Flask(__name__)
api = Api(app)


class ModelResponse(Resource):
    def get(self, query: str=""):
        parser = reqparse.RequestParser()
        parser.add_argument("query")
        params = parser.parse_args()
        query = params.get("query")
        answer = get_answer(query)
        return {
            "answer": answer
        }, 200


api.add_resource(ModelResponse, "/model", "/model/")
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
