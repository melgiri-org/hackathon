import json
import requests as req

def get_stat():
    r = req.post('http://127.0.0.1:5001/', data=f'type=get')
    r = json.loads(r.content)['data']
    return r

def add(user, amt):
    r = req.post('http://127.0.0.1:5001/', headers={"Content-Type":'application/x-www-form-urlencoded'}, data=f'type=add&data={user}|{amt}')
    return r.content

def remove(user, amt):
    r = req.post('http://127.0.0.1:5001/', headers={"Content-Type":'application/x-www-form-urlencoded'}, data=f'type=remove&data={user}|{amt}')
    return r.content