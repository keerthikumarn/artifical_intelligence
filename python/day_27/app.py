from flask import Flask, render_template
import os
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://admin:mydb123@python-in-30-days.coxwj7q.mongodb.net/"
client = MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
   port = int(os.environ.get("PORT", 5002))
   app.run(debug=True, host='localhost', port=port)
