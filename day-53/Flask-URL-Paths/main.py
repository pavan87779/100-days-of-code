from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello world!</h1>'

@app.route("/bye")
def bye():
    return "<h1>bye</h1>"

@app.route("/<name>/<int:number>")
def greet(name,number):
    return f"<h1>Helllo, {name},your are {number} years old</h1>"

if __name__ == "__main__":
    app.run(debug=True)