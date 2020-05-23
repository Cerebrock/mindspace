
# coding: utf-8

# In[12]:


import subprocess
import requests
import json
import os
import re
from time import sleep


# In[4]:


path = r"C:\Users\mgrinberg\Desktop\disc c\Investigación\Neurocomp"
    
def start_server():
    os.chdir(path +'\other\server')
    os.system(r"call C:\Users\mgrinberg\AppData\Local\Continuum\anaconda3\Scripts\activate.bat")
    os.system("set FLASK_APP=srv.py")
    os.system("start python srv.py")
    return None


# In[5]:


def get_tunnel():
    localhost_url = "http://localhost:4040/api/tunnels" #Url with tunnel details
    tunnel_url = requests.get(localhost_url).text #Get the tunnel information
    j = json.loads(tunnel_url)
    tunnel_url = j['tunnels'][0]['public_url']
    if 'https' not in tunnel_url:
        tunnel_url = j['tunnels'][1]['public_url']
    return tunnel_url

def replace_ngrok(tunnel_url):
    path_idx = '\index.html'
    with open(path + path_idx, 'r+') as file:
        html = file.read()
        html = re.sub('(https*://.+ngrok.+)/postdata', tunnel_url + '/postdata', html)
        file.seek(0)
        file.write(html)
    print('URL inserted', url)


# In[6]:


def commit_git(usr='cerebrock', repo = 'mindspace', passw = ''):
    os.chdir(path)
    os.system(f"git remote set-url origin https://{usr}:{passw}@github.com/cerebrock/{repo}.git")
    os.system("git add *")
    os.system("git commit -m 'auto'")
    os.system("git push origin master")
    return None


# In[ ]:


if __name__ == '__main__':
    passw = input('Ingresar password: \n')
    start_server()
    while True:
        os.chdir(path +'\other\server')
        os.system("start ngrok http 5000")
        sleep(20)
        url = get_tunnel()
        replace_ngrok(url)
        sleep(5)
        commit_git(passw=passw)
        sleep(28000)
        os.system(r'taskkill /f /im ngrok.exe')

