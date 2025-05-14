from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route('/')
def home():
    history = session.get('history', [])
    return render_template('index.html', result='', history=history)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
    except Exception as e:
        result = "Error: " + str(e)

    # سجل العمليات
    history = session.get('history', [])
    history.append(f"{expression} = {result}")
    session['history'] = history

    return render_template('index.html', result=result, history=history)

@app.route('/clear')
def clear():
    session.pop('history', None)
    return render_template('index.html', result='', history=[])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

