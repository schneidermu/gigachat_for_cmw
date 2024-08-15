from flask import Flask, request
from flask_restful import Api, Resource, reqparse

from get_response import get_answer

app = Flask(__name__)
api = Api(app)


class ModelResponse(Resource):
    def get(self, query: str=""):
        query = request.args.get('query')
        answer = get_answer(query)
        with open("output.txt", "w") as file:
            file.write(f"Запрос: {query}\n")
            file.write(f"Ответ: {answer}\n")
        with open("output.bin", "wb") as binary_file:
            binary_file.write(f"Запрос: {query}\n".encode('utf-8'))
            binary_file.write(f"Ответ: {answer}\n".encode('utf-8'))
        return {
            "answer": answer
        }, 200


api.add_resource(ModelResponse, "/model", "/model/")
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
