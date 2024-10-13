from flask import Flask, request, jsonify

app = Flask(__name__)

# Inicializa la lista de todos con dos elementos
todos = [
    {"done": False, "label": "Dummy Todo"},
    {"done": False, "label": "Dummy Todo 2"}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos), 201  # Aquí se devuelve 201 Created

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):
        deleted_todo = todos.pop(position)
        return jsonify({"message": "Todo deleted", "deleted": deleted_todo}), 200
    else:
        return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
