from dataclasses import dataclass
from fastapi import HTTPException
from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id : str
    name : str
    age : int

students : Dict[str , Student] = {}

@app.get("/hello")
def root():                 #
    return "Student API"

@app.get("/students")          #get ගන්නවා
def get_student():
    return list(students.values())

@app.post("/students")                  #create object
def create_student(student : Student):
    students[student.id] = student
    return {"message" : "successfully Created student !" , "student" : student}

# @app.put("/students/{student_id}")          #update object
# def update_student(student_id : str , student : Student):
#     if update_student not in students.keys():
#         raise HTTPException(status_code=404 , detail="Student id not found !")
#
#     students[student.id] = student
#     return {"message": "successfully update student", "student": student}

@app.put("/students/{student_id}")                  #update
def update_student(student_id: str, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student id not found!")

    students[student_id] = student
    return {"message": "successfully updated student", "student": student}

# @app.delete("/students/{student_id}")
# def delete_student(student_id : str , student : Student):
#     if student_id not in students.keys():
#         raise HTTPException(status_code=404 , detail="Student id not found !")
#
#     del_st = students.pop(student_id)
#     return {"message": "successfully delete student", "student": del_st}

@app.delete("/students/{student_id}")           #delete
def delete_student(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student id not found!")

    del_st = students.pop(student_id)
    return {"message": "successfully deleted student", "student": del_st}