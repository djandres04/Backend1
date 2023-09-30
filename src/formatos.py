import requests
from flask import jsonify
import json

'''
def luces():
    urldoor = "http://192.168.0.199:5000/light"
    entrada =  requests.get(urldoor)
    v1 = entrada.json()
    #print(v1)
    print(v1[2]["id"])
    #stado = v1["status"]
    #id = v1["id"]
    #return [stado,id]

def door(v1,v2):
    urljuan = ("http://192.168.0.199:5000/door/"+v1)
    print(urljuan)
    entrega = {"id":v1,"status":v2}
    entrega2 = json.dumps(entrega)
    requests.post(urljuan,json=entrega2)
    print(entrega2)

def light(v1,v2):
    urljuan = ("http://192.168.0.199:5000/light/"+v1)
    entrega = {"id":v1,"status":v2}
    entrega2 = json.dumps(entrega)
    requests.post(urljuan,json=entrega2)
    print(entrega2)

def buzz(v1,v2):
    urljuan = ("http://192.168.0.199:5000/buzzer/"+v1)
    entrega = {"id":v1,"status":v2}
    entrega2 = json.dumps(entrega)
    requests.post(urljuan,json=entrega2)
    print(entrega2)

def temp(v1,v2):
    urljuan = ("http://192.168.0.199:5000/temp/")
    entrega = {"id":v1,"status":v2}
    entrega2 = json.dumps(entrega)
    requests.post(urljuan,json=entrega2)
    print(entrega2)



'''