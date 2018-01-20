from flask import Flask

app = Flask(__name__)

@app.route('/')    #decorator- way to wrap a function and modify its way
def index():
    return 'This is my first app in Flask'

if __name__ == '__main__':
    app.run(debug=True)
