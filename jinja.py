import jinja2

env = jinja2.Environment()
template = env.from_string("Hi {{ their_name }}, my name is {{ my_name }}.")
print(template.render(their_name="John", my_name="Mary"))

import jinja2

env = jinja2.Environment()
template = env.from_string("""
My favorite fruits are:
{% for fruit in fruits -%}
- {{ fruit }}
{% endfor %}
""")
print(template.render(fruits=["apples", "oranges"]))