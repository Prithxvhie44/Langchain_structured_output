
from typing import TypedDict

class Person(TypedDict):

    name:str
    age:int

person1:Person = {
    "name":"Alice",   
    "age":30
}

Person2:Person = {
    "name":"Bob",
    "age":"25"}

print(person1)
print(Person2)