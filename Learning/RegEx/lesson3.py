import re
text = 'lat=5, lon = 7, a= 98, lon =6'

match1 = re.findall(r'lat\s*=\s*\d+|lon\s*=\s*\d+', text)  # У такого способа явный недостаток - надо дважды указать одну и ту же часть регулярки
print(match1)  # ['lat=5', 'lon = 7', 'lon =6']

match2 = re.findall(r'(lat|lon)\s*=\s*\d+', text)  # Сохраняющие скобки показывают второй уровень сохранения, то есть просто вхождения(сами слова) этих lat, lon
print(match2)  # ['lat', 'lon', 'lon']

match3 = re.findall(r'(?:lat|lon)\s*=\s*\d+', text)  # А вот такая запись говорит что надо убрать сохраняющие скобки и отдать оба уровню в изначальном виде
print(match3)  # ['lat=5', 'lon = 7', 'lon =6']

match4 = re.findall(r'((lat|lon)\s*=\s*\d+)', text)
print(match4)  # [('lat=5', 'lat'), ('lon = 7', 'lon'), ('lon =6', 'lon')]

match5 = re.findall(r'(lat|lon)\s*=\s*(\d+)', text)
print(match5)  # [('lat', '5'), ('lon', '7'), ('lon', '6')]

match6 = re.findall(r'(lat|lon)\s*=\s*(?:\d+)', text)
print(match6)  # ['lat', 'lon', 'lon']


# Чтобы назначить имя для группы есть следующий синатксис:
# создание --- (?P<name>)
# обращение --- (?P=name)
text1 = '<p> Image <img src="photo.jpg"></p>'
img_match = re.findall(r'<img\s+[^>]*src=(?P<srcname>\'|")(.+?)(?P=srcname)', text1)
print(img_match) # [('"', 'photo.jpg')]
