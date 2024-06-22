import yaml

print(yaml.dump(my_books[0].dict())) # type: ignore

from pydantic_core import to_jsonable_python

print(yaml.dumps(to_jsonable_python(my_books))) # type: ignore