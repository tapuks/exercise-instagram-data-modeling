import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250), nullable=False)
    email = Column(String(25),nullable=False)
    password = Column(String(25),nullable=False)
    is_active = Column (String(250))
    promo = Column (String(50), nullable=False)

class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250))
    email = Column(String(25),nullable=False)
    password = Column(String(25),nullable=False)
    linkedin = Column(String(250))
    type_of_teacher = Column(String(250))
    is_active = Column (String(250))
    promo = Column (String(50), nullable=False)
    # user_id= Column(Integer, ForeignKey('user.id'))
    # user=relationship(User)
    # post_id= Column(Integer, ForeignKey('post.id'))
#     # post=relationship(Post)

class School(Base):
    __tablename__ = 'school'
    id = Column(Integer, primary_key=True)
    name = Column (String(250))
    img_url = Column (String(250))
    # user_id = Column(Integer, ForeignKey('user.id'))
    # user=relationship(User)

class School_student(Base):
    __tablename__ = 'school_student'
    student_id = Column(Integer, ForeignKey('student.id'),primary_key=True)
    school_id = Column(Integer, ForeignKey('school.id'),primary_key=True)
    student = relationship(Student)
    school = relationship(School) 

class School_teacher(Base):
    __tablename__ = 'school_teacher'
    teacher_id = Column(Integer, ForeignKey('student.id'),primary_key=True)
    school_id = Column(Integer, ForeignKey('school.id'),primary_key=True)
    teacher = relationship(Teacher)
    school = relationship(School)  

class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    dynamsim = Column(Integer())
    pasion = Column(Integer())
    practises_example = Column(Integer())
    near = Column(Integer())
    date_teacher = Column(String(250))
    more_info = Column(String(500), unique=False, nullable=True)
    gif = Column(String(50), unique=False, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship(Teacher)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)

class Alumn_teacher(Base):
    __tablename__ = 'alumn_teacher'
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship(Teacher)
    student_id = Column(Integer, ForeignKey('student.id'))
    student = relationship(Student)

# class Media(Base):
#     __tablename__ = 'media'
#     id = Column(Integer, primary_key=True)
#     url = Column(String(250))
#     post_id = Column(Integer, ForeignKey('post.id'))
#     post= relationship(Post)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e