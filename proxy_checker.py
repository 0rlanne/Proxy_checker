import urllib.request , socket
import requests
import sys
api = "http://ip-api.com/json/"

socket.setdefaulttimeout(120)
ip = "219.92.3.149"
port = "8080"

proxyList = [ip + ":" + port] #use that model for implement ur code in a index or oder code 

sys.stdout.flush()

def proxy_test(pip):    
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  
    
    except urllib.error.HTTPError as e:        
        print('Error code: ', e.code)
        return e.code
    except Exception as detail:

        print( "ERROR:", detail)
        return 1
    return 0



data = requests.get(api+ip).json()

for item in proxyList:
    if proxy_test(item):
        print ("Proxy mort", item)
    else:
        print (item, "Fonctionne ")
        print ("[Pays]:", data['country'])

p = input("")