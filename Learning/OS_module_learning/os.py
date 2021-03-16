import os


# os.name
'''
При доступе к os.name, вы получите информацию о том, с какой платформой вы работаете. 
Вам откроются следующие значения: ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’, ‘riscos’
'''
print(os.name)
# nt
'''
Это говорит нам о том, что наш экземпляр Пайтон работает в окне Windows. 
Как мы об этом узнали? Майкрософт начали называть свою операционную систему NT много лет назад. 
Например, Windows 7 также носит имя Windows NT 6.1.
'''


# os.environ, os.getenv()
'''
Значение os.environ известно как объект мэппинга (сопоставления), 
который работает со словарем переменных пользовательской среды. 
Возможно вы не знали, но каждый раз, когда вы пользуетесь своим компьютером, некоторые переменные среды уже установлены.

Это дает вам полезную информацию, такую как количество процессоров, тип ОЗУ, имя компьютера, и так далее.
'''
print(os.environ)
# 'ALLUSERSPROFILE': 'C:\\ProgramData',
# 'APPDATA': 'C:\\Users\\mike\\AppData\\Roaming',
# 'CLASSPATH': '.;C:\\Program Files\\QuickTime\\QTSystem\\QTJava.zip',
# 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
# 'COMPUTERNAME': 'MIKE-PC',
# 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe',
# 'FP_NO_HOST_CHECK': 'NO',
# 'HOMEDRIVE': 'C:',
# 'HOMEPATH': '\\Users\\mike',
# 'LOCALAPPDATA': 'C:\\Users\\mike\\AppData\\Local',
# 'LOGONSERVER': '\\\\MIKE-PC',
# 'NUMBER_OF_PROCESSORS': '2',
# 'OS': 'Windows_NT',
# 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC',
# 'PROCESSOR_ARCHITECTURE': 'x86',
# 'PROCESSOR_IDENTIFIER': 'x86 Family 6 Model 15 Stepping 13, GenuineIntel',
# 'PROCESSOR_LEVEL': '6',
# 'PROGRAMDATA': 'C:\\ProgramData',
# 'PROGRAMFILES': 'C:\\Program Files',
# 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\',
# 'PUBLIC': 'C:\\Users\\Public',
# 'PYTHONIOENCODING': 'cp437',
# 'QTJAVA': 'C:\\Program Files\\QuickTime\\QTSystem\\QTJava.zip',
# 'SESSIONNAME': 'Console',
# 'SYSTEMDRIVE': 'C:',
# 'SYSTEMROOT': 'C:\\Windows',
# 'TEMP': 'C:\\Users\\mike\\AppData\\Local\\Temp',
# 'TMP': 'C:\\Users\\mike\\AppData\\Local\\Temp',
# 'USERDOMAIN': 'mike-PC',
# 'USERNAME': 'mike',
# 'USERPROFILE': 'C:\\Users\\mike',
# 'VBOX_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\',
# 'VS90COMNTOOLS': 'C:\\Program Files\\Microsoft Visual Studio 9.0\\Common7\\Tool\s\\',
# 'WINDIR': 'C:\\Windows',
# 'WINDOWS_TRACING_FLAGS': '3',
# 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log',
# 'WINGDB_ACTIVE': '1',
# 'WINGDB_PYTHON': 'c:\\python27\\python.exe',
# 'WINGDB_SPAWNCOOKIE': 'rvlxwsGdD7SHYIJm'}
'''
Переменная environ вернула словарь. 
Это значит, что вы можете получить доступ к значениям среды, пользуясь обычными словарными методами. 
Например:
'''
print(os.environ["TMP"])
# C:\Users\BOHDAN~1\AppData\Local\Temp
'''
Tакже можете использовать функцию os.getenv для доступа к этой переменной.

Полезность использования os.getenv() вместо словаря os.environ заключается в том, 
что если вы находитесь в положении, когда вам нужно получить доступ к переменной среды, 
которая не существует, функция getenv() вернёт объект None. 
Если вы попытаетесь сделать то же самое, пользуясь os.environ, вы получите уведомление об ошибке
'''


# os.chdir() и os.getcwd()
'''
Функция os.chdir позволяет нам вносить изменения в каталоге, который мы в данный момент используем в сессии. 
Если вам нужно знать, какой путь вы в данный момент используете, для этой нужно вызвать os.getcwd(). 
'''
print(os.getcwd())  # "C:\Users\Bohdana_Photos\Desktop\pycharm
os.chdir(r"C:\Users\Bohdana_Photos\Programs\Python\Python39\pycharm")
print(os.getcwd())  # C:\Users\Bohdana_Photos\Programs\Python\Python39\pycharm


# os.mkdir() и os.makedirs()
'''
Эти два метода используются для создания папок. 
Первая, os.mkdir(), позволяет создать одну папку.
Функция os.makedirs() создает промежуточные папки в пути, если их там нет. 
В целом, это значит, что вы создали путь, в котором размещены папки.
'''


# os.remove() и os.rmdir()
'''
Функции os.remove() и os.rmdir() используются для удаления файлов и каталогов соответственно.
'''


# os.rename(src, dst)
'''
Функция os.rename() применяется тогда, когда нужно переименовать файл или папку
'''


# os.startfile()
'''
Метод os.startfile() позволяет нам «запустить» файл в привязанной к нему программе. Другими словами, 
мы можем открыть файл вместе с привязанной к нему программой, как когда вы открываете файл PDF двойным щелчком,
и он открывается в программе Adobe Reader.
'''
os.startfile(r'C:\Users\Bohdana_Photos\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram')


# os.walk()
'''
Метод os.walk() дает нам возможность для итерации на корневом уровне пути. 
Это значит, что мы можем назначить путь к этой функции и получить доступ ко всем её подкаталогам и файлам.
'''
path = r'C:\Users\Bohdana_Photos\Downloads\Telegram Desktop'
for i in os.walk(path):
    for root in os.walk(path):
        print(*root, sep='\n')
        print(type(root))
        r'''
        'C:\\Users\\Bohdana_Photos\\Downloads\\Telegram Desktop', 
        [], 
        ['52b9354e-baac-4c5a-b94b-f2e5d7750453.jpg', 
        'image_2020-12-11_15-22-00.png',
        'image_2020-12-11_23-42-41.png',
        'image_2020-12-14_21-15-59.png',
        'image_2020-12-14_23-36-19.png',
        'image_2020-12-14_23-48-43.png',
        'image_2020-12-29_23-22-39.png',
        'tg_image_1015290227.jpeg',
        'tg_image_2167827455.jpeg',
        'tg_image_3888001203.jpeg',
        'tg_image_67269840.jpeg', 
        '__boilerplate.zip',
        'Почему не запускается.png', 
        'Снимок (2).PNG',
        'Снимок (3).PNG',
        'Снимок (4).PNG',
        'Снимок экрана от 2021-01-02 22-30-25.png',
        'Снимок экрана от 2021-01-02 22-34-21.png',
        'Снимок экрана от 2021-01-03 00-16-42.png',
        'Снимок.PNG']
        
        <class 'tuple'>
        '''


# OS.PATH
# OS.PATH
# OS.PATH
# OS.PATH
# OS.PATH
# OS.PATH
# OS.PATH
# OS.PATH
# OS.PATH
# OS.PATH


# os.path.basename
'Функция basename вернет название файла пути.'
print(os.path.basename(r'C:\Users\Bohdana_Photos\Downloads\Telegram Desktop'))


# os.path.dirname
'Функция dirname возвращает только только путь к указанному файлу|папке'
print(os.path.dirname(r'D:\VIKTOR\CANON pictures\IMG_05799(1).jpg'))


# os.path.exists
'Функция exists говорит нам, существует ли файл, или нет. Все что вам нужно, это указать ему путь.'
print(os.path.exists(r'C:\Users\Bohdana_Photos\Downloads\Telegram Desktop'))  # True
print(os.path.exists(r'C:\Users\Bohdana_Photos\Downloads\Telegram Desktop\fake.py'))  # False


# os.path.isdir / os.path.isfile
'''
Методы isdir и isfile тесно связаны с методом exists, 
так как они также тестируют присутствие или отсутствие файлов или папок на тех или иных путях. 
Однако, isdir проверяет только пути к папкам, а isfile, соответственно, к файлам. 
Если вам нужно проверить путь, и не важно, папка это или файл, проще будет воспользоваться методом exists.
'''
print(os.path.isfile(r'C:\Users\Bohdana_Photos\Programs\Python\Python39\pycharm\parsing\some_file\parser.py'))  # True
print(os.path.isdir(r'C:\Users\Bohdana_Photos\Programs\Python\Python39\pycharm\parsing\some_file\parser.py'))  # False
print(os.path.isdir(r'C:\Users\Bohdana_Photos\Programs\Python\Python39\pycharm\parsing\some_file'))  # True
print(os.path.isfile(r'C:\Users\Bohdana_Photos\Programs\Python\Python39\pycharm\parsing\some_file'))  # False


# os.path.join
'Метод join позволяет вам совместить несколько путей при помощи присвоенного разделителя.'
print(os.path.join(r'C:\Users\Bohdana_Photos\Programs\Python\Python39\pycharm\parsing\some_file\proxies', 'fuck', 'py', 'pi'))
# C:\Users\Bohdana_Photos\Programs\Python\Python39\pycharm\parsing\some_file\proxies\fuck\py\pi'


# os.path.split
'Метод split разъединяет путь на кортеж, который содержит и файл и каталог.'
print( os.path.split(r'C:\Python27\Tools\pynche\ChipViewer.py') )
# ('C:\\Python27\\Tools\\pynche', 'ChipViewer.py')
'В данном примере показано, что происходит, когда мы указываем путь к файлу.'

print( os.path.split(r'C:\Python27\Tools\pynche') )
# (‘C:\Python27\Tools’, ‘pynche’))
'подпапка стала вторым элементом кортежа с остальной частью пути в первом элементе.'

dirname, fname = os.path.split(r'C:\Python27\Tools\pynche\ChipViewer.py')
print(dirname)
# C:\\Python27\\Tools\\pynche
print(fname)
# ChipViewer.py