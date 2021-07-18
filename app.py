import re
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

kinoko_count = 3
takenoko_count = 5
messages = ['Kinoko is wonrderful!', 'Takenoko is awesome!']

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/api/v1/votes')
def vote_api():
    return jsonify({'kinoko': kinoko_count, 'takenoko': takenoko_count})

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

    message_html = ''
    for i in range(len(messages)):
        message = messages[i]
        message = re.sub(r'&', r'&amp;', message)
        message = re.sub(r'<', r'&lt;', message)
        message = re.sub(r'>', r'&gt;', message)
        message = re.sub(r'\*(.+)\*', r'<strong>\1</strong>', message)
        message = re.sub(r'(\d{2,3})-\d+-\d+', r'\1-****-****', message)
        message_html += '<div class="alert {1}" role="alert">{0}</div>\n'.format(
            message, 'alert-warning ms-5' if i % 2 == 0 else 'alert-success me-5')

    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
