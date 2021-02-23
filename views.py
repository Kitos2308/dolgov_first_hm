from myframework import render
from myframework import Application

def main_view(request):

    # Используем шаблонизатор
    return '200 OK', render('base.html')


# def about_view(request):
#     # Просто возвращаем текст
#     return '200 OK', "About"




def create_course(request):
    return '200 ок', render('create_course.html')

def create_category(request):
    return '200 ok', render('create_category.html')


def course_list(request):

    return '200 OK', render('course_list.html')

def category_list(request):
    return '200 ok', render('category_list.html')


# def contact_view(request):
#     # Проверка метода запроса
#     if request['method'] == 'POST':
#         data = request['data']
#         title = data['title']
#         text = data['text']
#         email = data['email']
#         print(f'Нам пришло сообщение! Отправитель - {Application.decode_value(email)}, '
#               f'тема - {Application.decode_value(title)}, текст - '
#               f' {Application.decode_value(text)}.')
#         return '200 OK', render('contact.html')
#     else:
#         return '200 OK', render('contact.html')