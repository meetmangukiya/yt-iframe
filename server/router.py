# The name `main.py` will also probably change, it is not permanent!
# TMP

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def root():     # TMP
    return "You seem to have been stumbled upon a website that is probably not for you" \
            "unless you were invited too! Anyways, thanks for passing by!"

@app.route('/play')
def play():
    ids = request.args.getlist('id')
    return render_template('player.html', ids=ids)

if __name__ == "__main__":
    app.run(debug=True, port=2000)
