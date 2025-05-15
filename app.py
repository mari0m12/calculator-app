from flask import Flask, render_template, request, session
from flask_session import Session  # type: ignore

app = Flask(__name__)

# Configuration for session
app.secret_key = 'your_secret_key'  # Replace with a secure random key in production
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def home():
    """
    Render the main calculator page with the result and history.
    """
    history = session.get('history', [])
    return render_template('index.html', result='', history=history)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Handle calculation of the expression entered by the user.
    """
    expression = request.form['expression']
    
    try:
        # Evaluate the mathematical expression safely
        result = eval(expression, {"__builtins__": None}, {})
    except Exception as e:
        result = "Error: " + str(e)

    # Save calculation to session history
    history = session.get('history', [])
    history.append(f"{expression} = {result}")
    session['history'] = history

    return render_template('index.html', result=result, history=history)

@app.route('/clear')
def clear():
    """
    Clear the calculation history from the session.
    """
    session.pop('history', None)
    return render_template('index.html', result='', history=[])

if __name__ == '__main__':
    # Run the Flask app on all interfaces (useful inside Docker)
    app.run(host='0.0.0.0', port=5000)
