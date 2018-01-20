from flask import Flask

app = Flask(__name__)

@app.route('/')    #decorator- way to wrap a function and modify its way of behaviour
def index():
    return 'This is my Flask root !'

@app.route('/home')
def home():
     return '<h1>HOME PAGE!</h1>'

@app.route('/profile/<username>')
def profile(username):
    return "<h4>Hey there, %s !<h4>" % username

@app.route('/post/<int:post_id>')
def show_int(post_id):                 #doesn't need to be same as url
    return "<h2>Post ID: %s<h2>" % post_id

if __name__ == '__main__':
    app.run(debug=True)