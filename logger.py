import datetime
import os

def logger(function):
    def new_function(*a, **b):
        f = open('log_file.log', "a", encoding="utf8")
        now = datetime.datetime.now()
        result = function(*a, **b)
        path_file = os.path.dirname(os.path.abspath('log_file.log'))
        function_name = function.__name__
        f.write( f'\n{now.strftime("%d-%m-%Y %H:%M")}'
                 f'\nНазвание функции: {function_name}'
                 f'\nАргументы функции - {a}, {b}'
                 f'\nРезультат - {result}'
                 f'\nПуть к лог-файлу: {path_file}')
        return result
    return new_function