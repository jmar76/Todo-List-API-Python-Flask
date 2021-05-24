from flask import Flask
app = Flask(__name__)
@app.route('/todos', methods=['GET'])
def hello_world():
    todos = { "label": "My first task", "done": False }
    json_todos = flask.jsonify(todos)
    return json_todos
# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)