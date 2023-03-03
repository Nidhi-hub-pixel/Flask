from flask import Flask,jsonify,request
app=Flask(__name__)
tasks = [
     { 
    'id': 1, 
    'contact': u'1234534267', 
    'name': u'Raju', 
    'done': False 
    }, 
    { 
    'id': 2,
      'contact': u'7853796409', 
      'name': u'Rahul', 
      'done': False 
      }
        ]
#@app.route("/")def hello_world():return "Hello!"

@app.route("/get-data") 
def get_task(): 
    return jsonify({ "data" : tasks })

@app.route("/add-data", methods=["POST"]) 
def add_task(): 
    if not request.json: 
        return jsonify({ "status":"error", "message": "Please provide the data!" },400) 
    task = { 'id': tasks[-1]['id'] + 1, 
            'contact': request.json['contact'], 
            'name': request.json.get('name', "name"), 
            'done': False 
            } 
    tasks.append(task) 
    return jsonify({ "status":"success", "message": "Task added succesfully!" })
if (__name__ == "__main__"): 
    app.run(debug=True)