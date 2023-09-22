
print('Это основной модуль main.py, его имя в процессе выполнения программы:', __name__)


from pack_1.file_11 import a
from pack_2.pack_21.file_211 import b


print('a =', a)
print('b =', b)
