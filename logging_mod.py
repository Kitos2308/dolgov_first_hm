from reusepatterns.singletones import SingletonByName
import time


# Заметка, можно применить стратегию если добавить стратегию логирования
class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def log(self,occation):

        with open(self.name, 'a') as out:
            out.write('\n')
            out.write(occation + '\n')
            out.write("=====================================")
            out.close()



