from time import sleep
import threading
import requests
import json
from flask import Flask
import os
from random import randint
import shutil

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
        print "Sleep for 10 seconds"
        sleep(10)
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
    return 'Hello, nice World!'

@app.route('/download')
def downloader():
    print "cloning file"
    
    old_file = '/home/yuriy/serious_business/bigfile'
    r = randint(1, 1000)
    new_file = '/home/yuriy/serious_business/bigfile_new' + str(r)
    print new_file
    shutil.copy(old_file, new_file)
    print "Cloning complete"

    return 'Done'

@app.route('/check/<url_to_check>')
def check_url(url_to_check):
    #myresponse = checker(url_to_check)
    return checker(url_to_check)

app.run(threaded=True)