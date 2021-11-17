import json
from flask import Flask, render_template

app = Flask(__name__)

# Very secure "database" lol that just stores the count of times this page was accessed.
def get_count():
    with open('database.json') as f:
        data = json.load(f)
        data["count"] +=1

    with open('database.json', 'w') as f:
        json.dump(data, f)
    return data["count"]


@app.route("/")
def route():
    return render_template('template.html', person_num=get_count())

@app.route("/ping")
def routeb():
    return render_template('template.html', person_num=get_count())

if __name__ == "__main__":
    app.run(host="0.0.0.0", ssl_context=('cert.pem', 'privkey.pem'))
