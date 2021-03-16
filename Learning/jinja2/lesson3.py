from jinja2 import Template

# В дзиндзе есть много фильтров - штук, которые те или иные манипуляции над структурами данных, преобразовую их в нужный нам результат: строкии\html строки
# фильтры sum, max, minб random, replace
cars = [{'model': 'BMW', 'price': 100000},
        {'model': 'Wolkswagen', 'price': 72300},
        {'model': 'Audi', 'price': 60500}]

tpl_sum = 'The sum price of the cars is {{c | sum(attribute="price")}}'
tm = Template(tpl_sum)
msg = tm.render(c=cars)
print(msg)  # The sum price of the cars is 232800

tpl_max = 'The max price of the cars is {{c | max(attribute="price")}}'
tm1 = Template(tpl_max)
msg1 = tm1.render(c=cars)
print(msg1)  # The max price of the cars is {'model': 'BMW', 'price': 100000}

# Для того, чтобы в выводе был не словарь, а, к примеру, модель машини, надо сделать так: В скобки взять всё выражение(вместе с фильтром) и обратиться по ключу(в данном случае к ключу "model")
tpl_example_max = 'The max price of the cars is {{(c | max(attribute="price")).model}}'
tm_example = Template(tpl_example_max)
msg_example = tm_example.render(c=cars)
print(msg_example)  # The max price of the cars is BMW
# min работает по аналогичному принципу

tpl_random = 'Car: {{ c | random }}'
tm2 = Template(tpl_random)
msg2 = tm2.render(c=cars)
print(msg2) # вывод: "Car: {} - любой из словарей

tpl_replace = 'Car: {{c | replace("a", "A")}}'
tm3 = Template(tpl_replace)
msg3 = tm3.render(c=cars)
print(msg3)  # Car: [{'model': 'BMW', 'price': 100000}, {'model': 'WolkswAgen', 'price': 72300}, {'model': 'Audi', 'price': 60500}]




# Блок filter - {% filter <filter name> %}___{{to what it do}}___{% endfilter %}
tpl_filter = '''
{%- for c in cars -%}
{% filter replace('B', '') %}{{ c.model }}{% endfilter %}
{% endfor -%}
'''
tm4 = Template(tpl_filter)
msg4 = tm4.render(cars=cars)
print(msg4)
''' 
MW
Wolkswagen
Audi
'''




### DRY - Don't Repeat Yourself
# macros
html_macro = '''
{% macro href(protocol, domain, url) -%}
    href="{{ protocol }}//:{{ domain }}.com/{{ url }}"
{%- endmacro %}

<a {{ href('http', 'porno365', '6978&^5457^5') }}>1</a>
<a {{ href('http', 'runetki', '9087234675$^&3%4^%$#&') }}>2</a>
<a {{ href('http', 'brazzers','^&*876%%$&^%$') }}>3</a>
'''
tm5 = Template(html_macro)
msg5 = tm5.render()
print(msg5)


# call - вложенный макрос
cars2 = [{'model': 'BMW', 'price': 100000, 'year': 2019},
        {'model': 'Wolkswagen', 'price': 72300, 'year': 2011},
        {'model': 'Audi', 'price': 60500, 'year': 2017}]

html_call = '''
{%- macro lst(lst_cars) %}
<ul>
{%- for c in lst_cars %}
    <li>{{c.model}} {{caller(c)}}
{%- endfor %}
</ul>
{%- endmacro %}

{%- call(car) lst(cars) %}
        <ul>
        <li>year: {{car.year}}
        <li>price: {{car.price}}
        </ul>
{%- endcall %}
'''

tm6 = Template(html_call)
msg6 = tm6.render(cars=cars2)
print(msg6)
