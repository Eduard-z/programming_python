import sys

print(sys.platform)             # название операционной системы
print(sys.maxsize)              # наибольшее целое число, поддерживаемое аппаратной платформой
print(sys.version)              # номер версии интерпретатора Python
if sys.platform[:3] == 'win': print('hello windows')
print(sys.path)                 # Путь поиска модулей
print(list(sys.modules.keys())) # все модули, загруженные программой
print(sys.exc_info())           # класс последнего исключения, его экземпляр и объект с трассировочной информацией
print(sys.argv)                 # Аргументы командной строки
