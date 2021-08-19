from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import random
from flask import Flask
app = Flask(__name__)

def generate_rdum():
    response = [200, 500]
    ran_resp=random.choice( response )
    return ran_resp

@app.route('/serviceA')
def response_rdum():
    res=generate_rdum()
    return str(res)
if __name__ == '__main__':
    run_simple('localhost', 5001, app)
