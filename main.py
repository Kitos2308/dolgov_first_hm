from myframework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/create-category/': views.create_category,
    '/create-course/': views.create_course,
    '/course-list/': views.course_list,
    '/category-list/': views.category_list,

}

def secret_controller(request):
    # пример Front Controller
    request['secret_key'] = 'Долгов Никита'




front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)


