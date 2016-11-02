# The name `main.py` will also probably change, it is not permanent! 
# TMP

from flask import flask 
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def root():     # TMP
    return "You seem to have been stumbled upon a website that is probably not for you" \
            "unless you were invited too! Anyways, thanks for passing by!"
            
@app.route('/play')
def play():
    return render_template()    # TODO -- Has to be implemented
