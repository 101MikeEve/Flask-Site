from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template ("gl.html")


@app.route('/1')
def page1():
    return render_template("index.html", id=1)


@app.route('/2')
def page2():
    return render_template("index.html", id=2)


@app.route('/3')
def page3():
    return render_template("index.html", id=3)


@app.route('/4')
def page4():
    return render_template("index.html", id=4)


@app.route('/5')
def page5():
    return render_template("index.html", id=5)


@app.route('/about')
def about():
    return render_template ("about.html")


@app.route('/<int:id>')
def user(id):
    return render_template('index.html', id=id)


if __name__ == "__main__":
    app.run(debug=True)