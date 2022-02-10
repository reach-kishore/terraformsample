import requests
import json


pullrequestURL = "https://api.github.com/repos/reach-kishore/terraformsample/pulls?q=is%3Apr+is%3Aopen+sort%3Aupdated-desc"

readPullURL = "https://api.github.com/repos/reach-kishore/terraformsample/pulls/PRNBR/files"


def getPR():
    payload={}
    headers = {
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json'
    }
    
    
    
    response = requests.request("GET", pullrequestURL, headers=headers, data=payload)
    
    return (json.loads(response.text)[0]['number'])

def readAddedFiles(prno):
    files = []
    
    readPullURL1 = readPullURL.replace("PRNBR",str(prno))
    payload={}

    payload={}
    headers = {
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", readPullURL1, headers=headers, data=payload)

    for i in json.loads(response.text): 
        if i["status"] == "added":
          files.append(i["filename"].split("/")[1])

    return files
prno = getPR()
filesadded = readAddedFiles(prno)
print(filesadded) 
