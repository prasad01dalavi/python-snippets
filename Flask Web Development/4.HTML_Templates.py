from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')    #decorator- way to wrap a function and modify its way of behaviour
def index():
    return '<h2>Home Page !</h2>'

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name_variable = name)

if __name__ == '__main__':
    app.run(debug=True)