from time import sleep
import threading
import requests
import json
from flask import Flask

app = Flask(__name__)
#app.debug = True

def checker(check_url):
    #app.run(threaded=True)
    # Conver URL to HTTP like view and send a request
    myurl="http://" + check_url
    print "Checking"
    go_on = False 
    try:
        res = requests.get(myurl)
        go_on = True
    except:
        print "Here is an ERROR"
        myresponse = "Wrong URL"
    # Getting values from the response
    if go_on:
        print "Sleep for 5 seconds"
        sleep(5)
        rtime = res.elapsed.total_seconds()
        rcode = res.status_code
        # Debugging string to check how it works. No needed anymore
        #myresponse = "This should check your URL in a future. The URL is {0}. Responce code is {1}. Time spent {2}".format(res,rcode,rtime)
        # Generate JSON response
        rres = {}
        rres['url'] = myurl
        rres['response_code'] = rcode
        rres['time'] = rtime
        myresponse = json.dumps(rres)
        
    #return myresponse
    return myresponse

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/check/<url_to_check>')
def check_url(url_to_check):
    #myresponse = checker(url_to_check)
    return checker(url_to_check)

app.run(threaded=True)
