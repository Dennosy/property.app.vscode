from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/map')
def map():
    return 'this is my map'

@app.route("/data")
def data():
    return "Welcome to my data page"

if __name__ == '__main__':                     
     app.run (debug=True)
