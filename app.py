from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
