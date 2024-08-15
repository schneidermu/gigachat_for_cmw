from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from get_response import get_answer

app = Flask(__name__)
api = Api(app)


class ModelResponse(Resource):
    def get(self, query: str=""):
        query = request.args.get('query')
        print("Запрос:", query)
        answer = get_answer(query)
        print("Ответ:", answer)
        text_bytes = answer.encode('utf-8')
        with open("output.bin", "wb") as binary_file:
            binary_file.write(text_bytes)
        return {
            "answer": answer
        }, 200


api.add_resource(ModelResponse, "/model", "/model/")
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
