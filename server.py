from flask import Flask
from flask_restful import Api, Resource

from get_response import get_answer

app = Flask(__name__)
api = Api(app)


class GigaChatResponse(Resource):
    def get(self, query: str=""):
        answer = get_answer(query)
        return answer, 200


api.add_resource(GigaChatResponse, "/gigachat", "/gigachat/")
if __name__ == '__main__':
    app.run(debug=True)
