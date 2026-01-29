from flask import Flask, render_template
import os
from pymongo import MongoClient
from bson.objectid import ObjectId # id object

MONGODB_URI = "mongodb+srv://admin:mydb123@python-in-30-days.coxwj7q.mongodb.net/"
client = MongoClient(MONGODB_URI)
print(client.list_database_names())

# Creating a database and collection
db = client.thirty_days_of_python
db.employees.insert_one({'name': 'Pradeep C', 'country': 'India', 'city': 'Bangalore', 'age': 36})
print(client.list_database_names())

# Inserting many documents to collection
students = [
        {'name':'Keerthi Kumar N','country':'IN','city':'Bangalore','age':40},
        {'name':'Pradeep','country':'FR','city':'Nice','age':36},
        {'name':'Chenna Reddy','country':'UK','city':'London','age':39},
    ]

for student in students:
   db.students.insert_one(student)
   
# MongoDB Find
student_data = db.students.find_one()
print(student_data)

print("Finding the student by id")
student_data_id = db.students.find_one({'_id':ObjectId('699e85b86f0dabf4bcb37e0c')})
print(student_data_id)

app = Flask(__name__)
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5002))
   app.run(debug=False, host='localhost', port=port)
