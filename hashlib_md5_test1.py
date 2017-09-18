'''
Created on 2017年9月18日

@author: jinx
'''
import hashlib

def calc_md5(password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
#t=calc_md5('shalslskhl')  
#print(t) 

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
    }

def login(user,password):
 
        if db[user] ==calc_md5(password):
            print('%s True' %user)
        else:
            print('%s False' %user)
        
login('michael','123456')
login('bob','888888')
login('alice','password')


