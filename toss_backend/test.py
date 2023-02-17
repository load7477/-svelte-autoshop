import requests as req

data = {   
    "amount": 1,
    "name": 1,
    "ingame": 1
}

req.get('http://localhost:5001/ingame:api', data=data)