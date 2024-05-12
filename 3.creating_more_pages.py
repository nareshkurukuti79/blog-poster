#-------------------- Creating a Flask App
# pipenv install psycopg2-binary
# pipenv install SQLAlchemy
# pipenv install flask
# pipenv shell

from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_topics():
    return render_template('home.html')

@app.route('/topic/<topic_id>')
def display_tasks(topic_id):
    return render_template('topic-tasks.html', topic_id=topic_id)

@app.route('/add/topic', methods=['POST'])
def add_topic():
    #add topic functionality

    return "Topic Added Successfully"


@app.route('/add/task/<topic_id>', methods=["POST"])
def add_task(topic_id):
    #add task functionality

    return "Task Added Successfully"

if __name__== '__main__':
    app.run(debug=True, host="127.0.0.1", port=5533)