import json
import hashlib
import flask
import flask_cors

a = flask.Flask('a')

flask_cors.CORS(a)

@a.errorhandler(400)
def aaa(e):
    print(e)
    return 's'

@a.route('/', methods=['POST'])
def i():
    r = flask.request.form
    print(r)
    match r['type']:        
        case "get":
            with open('index.json', 'r') as f:
                f = json.load(f)
            a = {}
            for i in range(0, len(f)):
                with open('lol/'+i, 'r') as f:
                    a[i] = f.read()
            return a

        case "add" | "remove":
            with open('index.json', 'r') as f:
                f = json.load(f)
            l = len(f)
            f[str(l)] = {
                "data":l,
                "next":None
            }
            f[str(l-1)]['next'] = hashlib.sha256(r['data'].encode()).hexdigest()
            with open('index.json', 'w') as ff:
                json.dump(f, ff)
            with open("lol/"+str(l), 'w') as f:
                f.write(r['data'].split('|')[0] + " " + r['type'] + " " + r['data'].split('|')[1])
            return "Done"

a.run(port=5001)