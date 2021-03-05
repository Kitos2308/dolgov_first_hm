from reusepatterns.prototypes import PrototypeMixin


# абстрактный пользователь
class User:
    def __init__(self, name):
        self.name=name


# преподаватель
class Teacher(User):
    pass


# студент
class Student(User):
    def __init__(self, name):
        self.courses = []
        super().__init__(name)



# Фабрика пользователей
class UserFactory:
    types = {
        'student': Student,
        'teacher': Teacher
    }

    @classmethod
    def create(cls, type_, name):
        return cls.types[type_](name)


# Категория
class Category:
    # реестр?
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.courses = []

    def course_count(self):
        result = len(self.courses)
        if self.category:
            result += self.category.course_count()
        return result

    def show_name_category(self):
        return self.name


# Курс
class Course(PrototypeMixin):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.courses.append(self)




# Интерактивный курс
class InteractiveCourse(Course):
    pass


# Курс в записи
class RecordCourse(Course):
    pass


# Фабрика курсов
class CourseFactory:
    types = {
        'interactive': InteractiveCourse,
        'record': RecordCourse
    }

    @classmethod
    def create(cls, type_, name, category):
        return cls.types[type_](name, category)


# Основной класс - интерфейс проекта
class TrainingSite:
    def __init__(self):
        self.teachers = []
        self.students = []
        self.courses = []
        self.categories = []



    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, id):
        print("++++++++++++++++++++++ID+++++++++++++++++++++++++++++++", id)
        for item in self.categories:
            print('item', item.id)
            if item.id == id:
                return item
        raise Exception(f'Нет категории с id = {id}')

    @staticmethod
    def create_course(type_, name, category):
        return CourseFactory.create(type_, name, category)

    def get_course(self, name) -> Course:
        for item in self.courses:
            if item.name == name:
                return item
        return None

    @staticmethod
    def create_user(type_, name):
        return UserFactory.create(type_, name)

    def get_course(self, name) -> Course:
        for item in self.courses:
            if item.name == name:
                return item

    def get_student(self, name) -> Student:
        for item in self.students:
            if item.name == name:
                return item
