from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def userLogin(name = None):
    return render_template('user.html', name_variable = name)

if __name__ == '__main__':
    app.run(debug=True)