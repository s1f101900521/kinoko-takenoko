import re
from flask import Flask, render_template, request
app = Flask(__name__)

kinoko_count = 3
takenoko_count = 5
messages = ['Kinoko is wonrderful!', 'Takenoko is awesome!']

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    global kinoko_count, takenoko_count, messages
    if request.form.get("item") == 'kinoko':
        kinoko_count += 1
    elif request.form.get("item") == 'takenoko':
        takenoko_count += 1

    messages.append(request.form.get("message"))
    if len(messages) > 3:
        messages = messages[-3:]
    
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_percent = takenoko_count / (kinoko_count + takenoko_count) * 100

    messages_data = []
    for i in range(len(messages)):
        messages_data.append((messages[i], 'alert-warning ms-5' if i % 2 == 0 else 'alert-success me-5'))

    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
