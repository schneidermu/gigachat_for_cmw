from gigachat import GigaChat


def get_answer(query):
    with GigaChat(credentials="", verify_ssl_certs=False, model='GigaChat-Plus') as giga:
        response = giga.chat(query)
        return response.choices[0].message.content