from  jinja2 import  Template

dct = {'name': 'Guli', 'year': 1997}
string = 'This string has been created in {{ d.year }} year'
tm = Template(string)
msg = tm.render(d=dct)
print(msg)