import websocket, json
import _thread as thread
import requests as req
bankpin = 


def on_message(ws, message):
    obj = json.loads(message)
    if obj["type"] == "push":
        push = obj["push"]

        try:
            title = push["title"]
            if "출금" in title or "송금" in title:
                return
        except:
            pass
        body = push["body"].replace("\n"," ")
        appname = push["package_name"]

        if appname == "viva.republica.toss":
            sp = body.split(" ")
            data = {
                'pamount': push["title"].replace("원 입금", "")
            }
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            req.post('http://localhost:5001/json:api', data=json.dumps(data), headers=headers)
            print(push["title"].replace("원 입금", " "))
        else:
            print("토스 제외 은행 불가.")

def on_error(ws, error):
    print("error:",error)

def on_close(ws):
    print("Closed")

def on_open(ws):
    print("Opened")
    

if __name__ == "__main__":
    #websocket.enableTrace(True)
    
    ws = websocket.WebSocketApp("wss://stream.pushbullet.com/websocket/"+bankpin,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()