from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ('<h1 style="text-align:center">Hello world!</h1>'\
            '<p style="text-align:center">This is a paragraph</p>' \
            '<div style="text-align:center">'
            '<img align-items="center" alt="Centered Image" height=600 style="text-align:center;" width=400 src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTFtaXdqZGs3MmxnMHJkNms1dHhtNThnd2MxYzEyZXZhems1aTJpMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y42OeCcJI4ufXDQ3oA/giphy.gif">'
            '</div>' )


if __name__ == "__main__":
    app.run(debug=True)