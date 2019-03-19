from flask import Flask, jsonify
from students import DbPlay


app = Flask(__name__)

@app.route("/")
def result():
	obj = DbPlay()
	return jsonify({'result': obj.data_processing()})

if __name__ == '__main__':
	app.run(debug=True)
