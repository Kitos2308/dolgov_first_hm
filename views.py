from myframework import render
from myframework import Application

def main_view(request):
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    return '200 OK', render('base.html', secret=secret)


def about_view(request):
    # Просто возвращаем текст
    return '200 OK', "About"



def contact_view(request):
    # Проверка метода запроса
    if request['method'] == 'POST':
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Нам пришло сообщение! Отправитель - {Application.decode_value(email)}, '
              f'тема - {Application.decode_value(title)}, текст - '
              f' {Application.decode_value(text)}.')
        return '200 OK', render('contact.html')
    else:
        return '200 OK', render('contact.html')