import random
from flask import Flask, abort, Response
app = Flask(__name__)

def generate_rdum():
    response = [200, 500]
    ran_resp=random.choice( response )
    return ran_resp

@app.route('/serviceA')
def response_rdum():
    res=generate_rdum()
    if res == 200:
        return str(res)
    else:
        abort(500)

@app.errorhandler(500)
def internal_error(error):
    return "500 error - Internal Server Exception", 500


if __name__ == '__main__':
    app.run('0.0.0.0', 5001)

