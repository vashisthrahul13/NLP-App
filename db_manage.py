import json

class Database():

    def add_user(self,name,email,password):
        try:
            with open('db.json','r') as rf:
                data = json.load(rf)
        except json.decoder.JSONDecodeError:
            data= {}
        if email in data:
            return 0
        
        else:
            data[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(data,wf)
            return 1
    
    def check_user(self,email,password):
        try:
            with open('db.json','r') as rf:
                data=json.load(rf)
        except FileNotFoundError:
            return 0
        
        if email in data:
            if  data[email][1] == password:
                return 1
            else:
                return 2
        else:
            return 0

