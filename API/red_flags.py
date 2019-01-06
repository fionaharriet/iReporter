from flask import Flask,request,jsonify

app = Flask(__name__)

red_flags = [{'incident':'bribery'}]

@app.route('/api/v1/red_flags',methods=['POST'])
def add():
    data = request.get_json()
    return jsonify(
        {
        'status':200,
        'data': data
        }
    )

@app.route('/api/v1/red_flags',methods=['GET'])
def get():
    return jsonify({
        'status':200,
        'data': red_flags
    })
