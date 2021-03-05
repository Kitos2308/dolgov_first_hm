from myframework import render, Application
from models import TrainingSite
from logging_mod import Logger, debug
from myframework.mycore_cbv import ListView, CreateView

# Создание копирование курса, список курсов
# Регистрация пользователя, список пользователей
# Логирование

site = TrainingSite()
logger = Logger('main')


def main_view(request):
    logger.log("main_view")
    print(f'Список курсов - {site.courses}')
    return '200 OK', render('course_list.html', objects_list=site.courses)


def create_course(request):
    if request['method'] == 'POST':
        # метод пост
        data = request['data']
        name = data['name']
        category_id = data.get('category_id')
        # print(category_id)
        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

            course = site.create_course('record', name, category)
            site.courses.append(course)
        # редирект?
        # return '302 Moved Temporarily', render('create_course.html')
        # Для начала можно без него
        return '200 OK', render('create_course.html')
    else:
        categories = site.categories
        return '200 OK', render('create_course.html', categories=categories)




class CreateStudentView(CreateView):
    template_name = "create_student.html"


    def create_obj(self, data: dict):
        name = data['name']
        name = Application.decode_value(name)
        new_obj = site.create_user('student', name)
        site.students.append(new_obj)








class CreateCategoryView(CreateView):
    template_name ="create_category.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = site.categories
        return context


    def create_obj(self, data: dict):

        name = data['name']
        name = Application.decode_value(name)
        category_id = data.get('category_id')


        category = None
        if category_id:
            category = site.find_category_by_id(int(category_id))

        new_category = site.create_category(name, category)
        site.categories.append(new_category)







def copy_course(request):
    request_params = request['request_params']

    try:
        name = request_params['name']
    except KeyError:
        print("empty request")

    old_course = site.get_course(name)
    if old_course:
        new_name = f'copy_{name}'
        new_course = old_course.clone()
        new_course.name = new_name
        site.courses.append(new_course)

    return '200 OK', render('course_list.html', objects_list=site.courses)

@debug
def category_list(request):
    logger.log('Список категорий')
    print("====================================================")
    print(site.categories)
    return '200 OK', render('category_list.html', objects_list=site.categories)

def course_list(request):
    logger.log('Список курсов')
    return '200, ok',  render('_course-list_.html', objects_list=site.categories)


# def all_course(request):
#
#     return '200, ok', render('course_list.html', objects_list=site.categories)



urlpatterns = {
    '/': main_view,
    '/create-course/': create_course,
    '/create-category/': CreateCategoryView(),
    '/copy-course/': copy_course,
    '/category-list/': category_list,
    '/_course-list_/': course_list,
    '/create-student/': CreateStudentView(),

    # '/_course-list_/(?P<pk>\d+)/$':all_course,

}


def secret_controller(request):
    request['secret'] = 'secret'


front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)


@application.add_route('/about/')
def about(request):
    return '200, ok', render('about.html')