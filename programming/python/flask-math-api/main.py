from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/cal/<int:n1><op><int:n2>', methods=['GET'])
@app.route('/cal/<float:n1><op><float:n2>', methods=['GET'])
def cal(n1,op,n2):
    return f"{n1} {op} {n2} = {n1 + n2}"

@app.route('/add/<num1>;<num2>', methods=['GET'])
@app.route('/add/<num1>+<num2>', methods=['GET'])
def add(num1, num2):
    try:
        num1, num2 = float(num1), float(num2)
    except ValueError:
        return jsonify({"error": "Parametry musí být čísla"}), 400
    result = num1 + num2
    return jsonify({"operation": "addition", "num1": num1, "num2": num2, "result": result}), 200

@app.route('/sub/<num1>;<num2>', methods=['GET'])
@app.route('/sub/<num1>-<num2>', methods=['GET'])
def subtract(num1, num2):
    try:
        num1, num2 = float(num1), float(num2)
    except ValueError:
        return jsonify({"error": "Parametry musí být čísla"}), 400
    result = num1 - num2
    return jsonify({"operation": "subtraction", "num1": num1, "num2": num2, "result": result}), 200

if __name__ == '__main__':
    app.run(debug=True)
