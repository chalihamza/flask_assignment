import math
import hashlib
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def printHome():
    return 'Home Page'


# write a flask api which use to get user name and print "hello user name"
@app.route("/new/<name>")
def helo(name):
    return f"hello {name}"


# write a flask api to find square of a given number
@app.route('/square/<int:num>', methods=['GET'])
def index(num):
    result = num ** 2
    print(result)
    return {'result': result}


# Create a Flask API, that accepts an image file and return its md5 hash. (you can use following code to generate md5
# hash of an image)
@app.route('/pathImage')
def pathImage2():
    return render_template('index.html')


@app.route('/getPath', methods=['GET', 'POST'])
def home():
    # global in_hash
    if request.method == 'POST':
        img = request.form['path']
        with open(img, "rb") as f:
            byte = f.read()
        in_hash = str(hashlib.md5(byte).hexdigest())

    return render_template('DisplayResult.html', result=in_hash)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4567)
    # app.run(debug=True, port=100)
