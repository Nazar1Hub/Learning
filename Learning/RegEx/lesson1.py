import re

# Поиск символов по группам через []
s = 'Email, food and some piece of 22 shit'
m = re.findall(r'\d|[Ee][mc]', s)  # \d - только цифры
print(m)  # ['Em', 'ec', '2', '2']

txt = 'Что-то -5 и даже 55'
tch = re.findall(r'[-0-9][0-9]', txt)
print(tch)  # ['-5', '55']

