import re

# {x} - ровно х раз
# {x, y} - от х до y
# {x, } - x и более раз
# {, y} - не более y раз
# ? ищет 0-1 вхождений
# + ищет 1+ вхождений
# * ищет 0+ вхождений

text = 'author=Pushkin A.S.; title = Evgeniy Onegin; price =200; year= 1895'
match = re.findall('\w+\s?=\s?[^;]+', text)
print(match)  # ['author=Pushkin A.S.', 'title = Evgeniy Onegin', 'price =200', 'year= 1895']

text1 = '<p> Proxy <img src="image.jpg"> in List </p>'
match1 = re.findall('<img\s+[^>]*?src\s*=\s*[^>]{2,}>', text1)
print(match1)  # ['<img src="image.jpg">']