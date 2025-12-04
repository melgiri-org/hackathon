import flask
import json
import base64
import os
import db_connect as dc
import sqlite3
import flask_cors


pwd = os.popen("pwd").read().strip()

cnx = sqlite3.connect(
    database=os.path.join(pwd, "user.db"),
    check_same_thread=False
)

cursor = cnx.cursor()


app = flask.Flask('Main')

flask_cors.CORS(app)
@app.route('/')
def index():
    try:
        if json.loads(base64.b64decode(flask.request.cookies['log'].encode()))['role'] == "admin":
            return flask.render_template('admin.html')
        return flask.render_template('member.html')
    except:
        return flask.render_template('login.html')

@app.route('/login', methods=["POST"])
def log():
    r = flask.Response("ok")
    r.set_cookie('log', base64.b64encode(str({"user":"admin", "role":"DAS"}).encode()))
    return r

@app.route('/bcs', methods=["POST"])
def bcs():
    dc.get_stat()
#TODO

@app.route('/dep', methods=["POST"])
def dep():
    user = flask.request.form['user']
    amt = flask.request.form['amt']
    dc.add(user, amt)
    cursor.execute("update user set amt = amt + " + amt + " where user = '"+user+"'")
    cnx.commit()
    return "Done"

@app.route('/wit', methods=["POST"])
def wit():
    user = flask.request.form['user']
    amt = flask.request.form['amt']
    cursor.execute("SELECT * FROM user where user = '" + user+"'")
    a = cursor.fetchall()[0][1]
    if a<int(amt):
        return "Cant withdraw"
    dc.remove(user, amt)
    cursor.execute("update user set amt = amt - " + amt+" where user = '"+user+"'")
    cnx.commit()
    return "Done"



# a = {
#     "pre":"",
#     "data":{
#         "trasid"
#         "from"
#         "to"
#         "amt"
#         "res"

#     },
#     "sign":"",
#     "conf":"",
#     "f-amt":''
# }

app.run(host='0.0.0.0')