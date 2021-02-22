from myframework import Application
import views

urlpatterns = {
    '/': views.main_view,
    '/create-course/': views.create_course,
    '/create-category/': views.create_category,
    '/copy-course/': views.copy_course,
    '/category-list/': views.category_list,

}

def secret_controller(request):
    # пример Front Controller
    request['secret_key'] = 'Долгов Никита'




front_controllers = [
    secret_controller
]

application = Application(urlpatterns, front_controllers)


