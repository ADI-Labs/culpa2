import requests
import json
from Models.Departments import department
from Models.Professors import professor
from Models.Courses import course
from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
import os

URI = "postgres://xeeqkeipvcflil:fead0f891152e8f657d7ee59ba256aa36c24fed629a0ee765b6a6aac6da2610f@ec2-54-225-236-102.compute-1.amazonaws.com:5432/d7mipabothqsm0"
engine = create_engine(URI)
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
