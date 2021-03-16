import os
with open('answer.txt', 'w') as new_py:
    new_py.write('\n'.join(sorted(list(set([tpl[0] for tpl in os.walk('main') for file in tpl[2] if file.endswith('.py')])))))


