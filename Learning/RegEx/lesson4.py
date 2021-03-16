import re

text = "подоходный прибыльный налог, прибыль которого - доход"
match = re.findall(r"\b(прибыль|обретение|доход)\b", text)  # Такая запись позволяет уменьшить громоздкость регулярки и сделать её более читабельной, вместо прописывания \b у каждого слова
print(match)  # ['прибыль', 'доход']

html_text = """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html charset=windows1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<script type="text/js">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>
"""

match1 = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", html_text, re.MULTILINE)
print(match1)  # ["\nlet o = document.getElementById('id_div');\nconsole.log(obj);\n"]

match2 = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", html_text, re.MULTILINE)
print(match2)  # ["\nlet o = document.getElementById('id_div');\nconsole.log(obj);\n</script>"]

match3 = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", html_text, re.MULTILINE)
к = re.findall(r'\b4(?!000)\d\d\d\b', '4010 4100 4200 4342 4000 5000 43782')
print(к)