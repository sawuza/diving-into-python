# open - открыть файл
f = open('filename')

# открытие файла на чтение
f = open('filename', 'w ')

# записать файл
f.write('hello world')

# закрыть файл
f.close()

# открытие файла на чтение и запись
f = open('filename', 'r+')

# чтение файла
f.read()

# для повторного прочтения нужно переместить указатель в начало
f.seek(0)

# чтение одной строки
f.readline()

# контекстный менеджер (можно не заботится о закрытии файла)
with open('filename') as f:
    print(f.read())
