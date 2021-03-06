import json
from flask import Flask, render_template,request,redirect
import logging

app = Flask(__name__)

logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('output.log')
logger.addHandler(handler)


def get_count():
    with open('database.json') as f:
        data = json.load(f)
        data["count"] +=1

    with open('database.json', 'w') as f:
        json.dump(data, f)
    return data["count"]


@app.route("/")
def route():
    logger.info(f"Incoming is :{request.remote_addr}")
    return render_template('template.html', person_num=get_count())


# If you're copying + pasting, don't do this in a real production.
# Use something like nginx.
@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=('/ssl/cert.pem', '/ssl/privkey.pem'))
