# app/schemas/teacher.py
from pydantic import BaseModel

class TeacherBase(BaseModel):
    name: str
    email: str

class TeacherCreate(TeacherBase):
    password: str

class Teacher(TeacherBase):
    id: int

    class Config:
        orm_mode = True
