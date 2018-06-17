import os

print(os.getpid())              # числовой идентификатор (ID) процесса
print(os.getcwd())              # текущий рабочий каталог
os.chdir(r'C:\Users')           # Если потребуется назначить текущим другой каталог
print(os.getcwd())
print(os.sep)                   # символ, который используется в качестве разделителя компонентов пути к каталогу
print(os.pathsep)               # символ, отделяющий каталоги в списках каталогов
print(os.pardir, os.curdir)     # указателей на родительский и текущий каталоги
print(repr(os.linesep))         # символ завершения строк в используемой системе
print(os.path.isdir(r'C:\Users'))   # является ли имя файла каталогом
print(os.path.isfile(r'C:\Users'))  # является ли имя файла простым файлом
print(os.path.isdir('nonesuch'))    # False
print(os.path.isfile('nonesuch'))   # False
print(os.path.getsize(r'C:\Users\admin\tilemill.log'))
name = r'/home/lutz/temp/data.txt'
print(os.path.dirname(name), os.path.basename(name))
print(os.path.abspath(''))          # пустая строка означает тек. раб. каталог (cwd)
print(os.system('dir'))             # Запускает команду оболочки из сценария Python
print(os.popen('dir').readlines())  # Запускает команду оболочки и соединяется с ее потоками ввода или вывода
# os.startfile("document.doc")    # open file in Microsoft Word
# os.startfile("myscript.py")     # run file with Python
print(list(os.environ.keys()))      # Переменные окружения оболочки
print(os.environ['WINDIR'])
print(os.listdir('.'))              # имена всех файлов в каталоге
print(list(os.walk('.')))           # имя текущего каталога, а также списки всех файлов и всех подкаталогов
print(os.path.join('.', 't.txt'))   # .\t.txt
