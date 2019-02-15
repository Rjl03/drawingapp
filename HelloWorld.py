from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "hello"


@app.route("/draw")
def draw():
    return render_template('drawing_circle.html')

@app.route("/about")
def about():
    return "This is about page"

if __name__ == "__main__":
    app.run()