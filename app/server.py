from flask import Flask, request
from flask_restful import Api, Resource

from get_response import get_answer

app = Flask(__name__)
api = Api(app)


class ModelResponse(Resource):
    def get(self, query: str=""):
        query = request.args.get('query')
        answer = get_answer(query)
        return {
            "answer": answer
        }, 200


class FileResponse(Resource):
    def get(self, query: str=""):
        question = request.args.get('question')
        content = request.args.get('content')

        # content = decode(content)

        query = f'Ты отвечаешь на вопросы по документам. Вот текст документа:\n\n{content}\n\nОтветь на вопрос:\n\n{question}\n\nОтвет:\n\n'
        answer = get_answer(query)
        return {
            "answer": answer
        }, 200


api.add_resource(ModelResponse, "/model", "/model/")
api.add_resource(FileResponse, "/file", "/file/") # сюда запрос отправляем для ответа на вопрос по документу

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')