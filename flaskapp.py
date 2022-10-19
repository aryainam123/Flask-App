from flask import Flask,jsonify, request

app = Flask(__name__)

list = [
    {
        'id': 1,
        'Name': u'Arya',
        'Contact': u'7662983278', 
        'Done': False
    },
    {
        'id': 2,
        'Name': u'Arnav',
        'Contact': u'9102984768', 
        'Done': False
    }
]


@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id': list[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'Done': False
    }
    list.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : list
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)