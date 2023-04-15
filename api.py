# Python scripy for Creating REST API 
from flask import Flask, jsonify

print("success")

app = Flask(__name__)

@app.route("/")

def welcomeFun():
    return "Hello welcome to flask"

@app.route("/<name>/")
def jsonFun(name):
    dis = {"Name": name, "age": 24, "qualifcation": "B.Tech", 
    "repeat": {"Name": name, "age": 25, "qualifcation": "M.Tech"},
    "List": {"Name": name, "age": 21, "qualifcation": "B.Tech"}}
    return jsonify(dis)
    
    
@app.route("/<name>")
def nameFun(name):
    return f"Hello {name} welcome to flask"
    
    
if __name__ == "__main__":
    app.run(debug=True)