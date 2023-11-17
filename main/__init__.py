from flask import Flask,redirect
import sys, os.path

app_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/main/')
sys.path.append(app_dir)
import routes 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return routes.hello_world()

@app.route("/post", methods = ['post'])
def post():
    routes.post()
    return redirect('/')

@app.route("/<name>")
def name(name):
    return routes.name(name)

if __name__ == "__main__":
    app.run(debug=True)