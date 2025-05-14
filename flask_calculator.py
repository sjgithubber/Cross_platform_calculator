from flask import Flask, render_template, request, jsonify
# from flaskwebgui import FlaskUI

app = Flask(__name__)

# ui = FlaskUI(app, width=500, height=500)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data.get('expression', '')
    
    try:
        # eval evaluates strings
        result = eval(expression)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    # Standard Flask app
    app.run(debug=True)
    
    # For desktop app using Flask-Desktop
    # import flask_desktop
    # flask_desktop.run(app, width=350, height=500, port=5000)
    # ui.run()
