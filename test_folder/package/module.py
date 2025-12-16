from requests import get

def get_question_data():
    response = (get('https://jsonkeeper.com/b/AGB2S')).json()
    return response

