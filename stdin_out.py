import sys

sys.stdout.write('hello stdout world' + '\n')   # стандартный поток вывода
text = sys.stdin.readline()[:-1]                # стандартный поток ввода
print(text)

from subprocess import Popen, PIPE, call

X = call('python module_sys.py')                # удобно: Hello shell world
pipe = Popen('python module_sys.py', stdout=PIPE)
print(pipe.communicate()[0])                    # (stdout, stderr)
print(pipe.returncode)                          # код завершения

pipe = Popen('python stdin_out.py', stdin=PIPE)
pipe.stdin.write(b'Pokey\n')
pipe.stdin.close()
print(pipe.wait())                              # код завершения
