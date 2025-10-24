from pydantic import BaseModel

class student(BaseModel):
    name:str


new_student={"name":"Prithviraj"}

st1=student(**new_student)

print(st1)