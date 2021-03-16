from jinja2 import Template, escape


### raw - блок, ползволяющий определить в строке часть, которая не будет рендериться 
data = 'Jinja module was created by {{name}}'
tm = Template(data)
msg = tm.render(name='ME')
print(msg)  # Jinja module was created by ME

data1 = '{% raw %}Jinja module was created by {{ name }}{% endraw %} and by {{ name1 }}'
tm1 = Template(data1)
msg1 = tm1.render(name='Somebody', name1='Artuz') #  name='Somebody' можно даже не указывать
print(msg1)  # Jinja module was created by {{ name }} and by Artuz




### '''флаг e'''  и  '''escape функция''' позволяют подать html код в строке в виде этого самого кода, вместо того, что будет сделано при обработке штмл файла
html_link_a = '<a href=\'#\'>something</a>'
tm2 = Template('{{link | e}}')  # link - это просто ссылка на строку, которую мы укажем при рендеринге
msg2 = tm2.render(link=html_link_a)
print(msg2)  # &lt;a href=&#39;#&#39;&gt;something&lt;/a&gt;
"Это те символы, которые  штмл файл расшифрует как текст в изначальном виде и не будет создававть ссылку, а именно  \"<a href=\'#\'>something</a>\""

html_link_a1 = '<a href=\'#\'>something</a>'
msg3 = escape(html_link_a1) # результат будет тот же, что и при обычном рендеринге через флаг "е" как в примере выше, только такая конструкция быстрее и занимает меньше места
print(msg3)  # &lt;a href=&#39;#&#39;&gt;something&lt;/a&gt;




# цикл for - {% for <expression> -%}___{% endfor %}
# а также услновный оп. if\elif\else - {% if <condition> %}___{% endif %}
cities_countries = [
    {'id': 5, 'country': 'Ukraine', 'city': 'Odessa'},
    {'id': 8, 'country': 'USA', 'city': 'Oklahoma-city'},
    {'id': 12, 'country': 'Belarus', 'city': 'Minsk'},
    {'id': 3, 'country': 'Belgium', 'city': 'Gent'}
]
link = '''<table class='countries_cities'>
{%- for cc in cities_countries %}
{%- if cc['id'] <= 5 %}
    <li>
        country - {{cc['country']}}
        <li>
            city - {{cc['city']}}
        </li>
    </li>
{%- elif 5 < cc['id'] <= 10 %}
    <li>
        coutry - cc['country']
        <li>
            city - permission denied
        </li>
    </li> 
{%- else %}
    <a href='#'>1</a>
{%- endif %}
{%- endfor %}
</table>'''  # минусики у for и endfor указывают где надо убрать перенос строки, а где - нет 
tm4 = Template(link)
msg4 = tm4.render(cities_countries=cities_countries) 
print(msg4)
'''
<table class='countries_cities'>
    <li>
        country - Ukraine
        <li>
            city - Odessa
        </li>
    </li>
    <li>
        coutry - cc['country']
        <li>
            city - permission denied
        </li>
    </li>
    <a href='#'>1</a>
    <li>
        country - Belgium
        <li>
            city - Gent
        </li>
    </li>
</table>
'''