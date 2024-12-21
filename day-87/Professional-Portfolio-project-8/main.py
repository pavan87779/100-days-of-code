from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Todo items
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Route: Home
@app.route("/")
def home():
    todo_list = Todo.query.all()  # Fetch all tasks
    return render_template("index.html", todo_list=todo_list)

# Route: Add a new task
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)  # Add to database
    db.session.commit()  # Commit changes
    return redirect(url_for("home"))

# Route: Update task status
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.get(todo_id)  # Get task by ID
    if todo:
        todo.complete = not todo.complete  # Toggle completion status
        db.session.commit()  # Commit changes
    return redirect(url_for("home"))

# Route: Delete a task
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get(todo_id)  # Get task by ID
    if todo:
        db.session.delete(todo)  # Delete task
        db.session.commit()  # Commit changes
    return redirect(url_for("home"))

# Run the application
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database and tables
    app.run(debug=True)
