from flask import Flask, request
from flask_restful import Api, Resource
import base64
import zipfile
import os
import xml.etree.ElementTree as ET
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
    def post(self, query: str=""):
        content_dict = request.json.get('Content')
        question = content_dict.get('question')
        content = content_dict.get('Content')

        # content = decode(content)

        query = f'Ты отвечаешь на вопросы по документам. Вот текст документа:\n\n{decoder(content)}\n\nОтветь на вопрос:\n\n{question}\n\nОтвет:\n\n'
        answer = get_answer(query)
        return {
            "answer": answer
        }, 200


def decoder(question):
    decoded_content = base64.b64decode(question)
    question = ''
    try:
        decoded_text = decoded_content.decode('utf-8')
        return decoded_text
    except UnicodeDecodeError:
        with open('decoded_content.bin', 'wb') as f:
            f.write(decoded_content)
    try:
        with zipfile.ZipFile('decoded_content.bin', 'r') as zip_ref:
            zip_ref.extractall('extracted_files')
    except zipfile.BadZipFile:
        question = 'Ошибка'
    def extract_text_from_xml(xml_file_path):
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        namespaces = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        }
        
        text_content = []
        for elem in root.findall('.//w:t', namespaces):
            if elem.text:
                text_content.append(elem.text)
        
        return ' '.join(text_content)
    word_folder = os.path.join('extracted_files', 'word')
    if os.path.exists(word_folder):
        for file_name in os.listdir(word_folder):
            if file_name.endswith('.xml'):
                file_path = os.path.join(word_folder, file_name)
                extracted_text = extract_text_from_xml(file_path)
                if extracted_text:
                    question += extracted_text
    else:
        print("Папка 'word' не найдена!")
    return question


api.add_resource(ModelResponse, "/model", "/model/")
api.add_resource(FileResponse, "/file", "/file/") # сюда запрос отправляем для ответа на вопрос по документу

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')