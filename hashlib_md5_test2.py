'''
Created on 2017年9月18日

@author: jinx
'''
import hashlib

def get_md5(str):
    md5=hashlib.md5()
    md5.update(str.encode('utf_8'))
    return(md5.hexdigest())


db={}
def register(username,password):
    db[username] = get_md5(password+username+'the_salt')
    
    
def login(username, password):
    if db[username]==get_md5(password):
        print('%s True' %username)
    else:
        print('%s False' %username)

register('ji','iloveu')
login('ji','iloveu')



