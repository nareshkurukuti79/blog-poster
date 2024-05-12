# *-*-*-* ----- **** ----- ------ ---------------------
# *-*-*-* ----- Connecting The Flask App to the Database Using SQLAlchemy
# pipenv install psycopg2-binary
# pipenv install SQLAlchemy
# pipenv install flask
# pipenv shell
# pipenv install Flask_SQLAlchemy //Need to connect flask application with dabase

from logging import debug
from flask import Flask, render_template, flash, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy
# How to generate a secret key
# enter python or python3 in the terminal
# import os
# os.urandom(24)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/blog_poster'

app.config['SECRET_KEY'] = '\x1b|\x88\xd9\xd5l\x9dFh?@\x8e\x04\xa7Z\xa3\xdd1i\xb5\xcf\xf3\xea\x05'

db = SQLAlchemy(app)


class Topic(db.Model):
    __tablename__ = 'topics'

    topic_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=255))

class Task(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topics.topic_id'))
    description = db.Column(db.String(length=255))

    topic = db.relationship("Topic")

@app.route('/')
def display_topics():
    return render_template('home.html', topics=Topic.query.all())


@app.route('/topic/<topic_id>')
def display_tasks(topic_id):
    return render_template("topic-tasks.html", 
                           topic = Topic.query.filter_by(topic_id=topic_id).first(), 
                           tasks = Task.query.filter_by(topic_id=topic_id).all())


@app.route('/add/topic', methods=["POST"])
def add_topic():
    # add topic functionality
    if not request.form["topic-title"]:
        flash("Enter a title for your new Topic", "tomato")
    else:
        topic = Topic(title=request.form['topic-title'])
        db.session.add(topic)
        db.session.commit()
        flash("Topic Added Successfully", "lawngreen")

    return redirect(url_for('display_topics'))

@app.route("/add/task/<topic_id>", methods=["POST"])
def add_task(topic_id):
    # add task functionality
    if not request.form["task-description"]:
        flash("Enter a task description", "tomato")
    else:
        task = Task(topic_id=topic_id, description=request.form['task-description'])
        db.session.add(task)
        db.session.commit()
        flash("Task Added Successfully", "lawngreen")

    return redirect(url_for('display_tasks', topic_id=topic_id))
    

    return "Task Added Successfully"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5533)
