from flask import Flask, send_file, request, render_template, jsonify
import requests, json
app = Flask(__name__)
import qrcode
from datetime import datetime
import asyncio as asy
# 일반적인 라우트 방식입니다.

def checkpushbullet(amount, name):
    return amount, name


@app.route('/toss:api', methods=['POST', 'GET'])
def board():
    if request.method == 'POST':
        amount = request.form['amount']
        global name
        name = request.form['name']
        ingame = request.form['ingame']
        if name.isdigit() == False and amount.isdigit() == True and name not in "'" and amount not in "'":
            print(request.form)
            img = qrcode.make(f'https://toss.me/loads/{amount}')
            type(img)  
            time = datetime.today().strftime('%Y-%m-%d-%H-%M-%S')
            img.save(f"toss_backend/static/{amount}-{name}.png")
            data = {
                "amount": amount,
                "name": name,
                "ingame": ingame
            }
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post('http://localhost:5001/json:api', data=json.dumps(data), headers=headers)
            res = requests.post('http://localhost:5001/ingame:api/', data=data)
            amount=amount
            name=name
            
            return render_template('index.html', amount=amount, name=name, display='none')
        else:
            return '비정상적으로 충전 신청을 하였습니다.'
    else:
        return '비정상적인 경로로 접속하셨습니다.'

@app.route('/json:api', methods=['POST', 'GET'])
def testapi():
    if request.method == 'POST':
        datas = json.loads(request.data)
        for value in datas['pamount']:
            data = {
                'amount': value,
                'name': name
            }
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            requests.post('http://localhost:5001/api:fivem', data=json.dumps(data), headers=headers)
        return jsonify(data)
    else:
        return '비정상적인 경로로 접속하셨습니다.'


@app.route('/api:fivem')
def apifivem():
    if request.method == 'POST':
        return jsonify(request.data)
    else:
        return 'GET으로는 접속이 불가합니다.'


app.run(host="localhost",port=5001)