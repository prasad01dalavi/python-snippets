from flask import Flask, request


app = Flask(__name__)

@app.route('/')    #decorator- way to wrap a function and modify its way of behaviour
def index():
    return '<h2>Requested Method: %s</h2>' % request.method

@app.route('/method',methods=['GET','POST'])    #decorator- way to wrap a function and modify its way of behaviour
def request_check():
    if request.method == 'POST':
        return 'You are using Post Method'
    else:
        return 'You probably using Get Method'


if __name__ == '__main__':
    app.run(debug=True)