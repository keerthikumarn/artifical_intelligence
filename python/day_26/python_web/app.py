'''
Python is a general purpose programming language and it can be used for many places. In this section, we will see how we use Python for the web. There are many Python web frame works. Django and Flask are the most popular ones. Today, we will see how to use Flask for web development.

Flask
Flask is a web development framework written in Python. Flask uses Jinja2 template engine. Flask can be also used with other modern front libraries such as React.
'''
from flask import Flask, render_template
import os

app = Flask(__name__)
@app.route("/")
def home ():
    #return '<h1>Welcome</h1>'
    return render_template('home.html')
    
@app.route('/about')
def about():
    #return '<h1>About us</h1>'
    return render_template('about.html')
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host='0.0.0.0', port=port)

	

