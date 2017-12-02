#!/usr/bin/python3

'''
 THIS EXAMPLE IS TAKEN FROM QUALYS COMMUNITY 
 URL: https://community.qualys.com/docs/DOC-4551 ; thanks to Brian.
'''
import requests
import xml.etree.ElementTree as ET
import time
 
def login(s):
    #
    # ---Session Login---
    #
    # Logs into a Qualys session given a requests.Session object 's'. A Session.post()
    # always returns a response, here assigned 'r'.
    #
    payload = {
               'action':'login',
               'username':'user',
               'password':'password'
               }
    r = s.post('https://qualysapi.qg2.apps.qualys.com/api/2.0/fo/session/', data=payload)
 
    # Now that all the hard work was done, lets parse the response.
    xmlreturn = ET.fromstring(r.text)
    print (xmlreturn)
    for elem in xmlreturn.findall('.//TEXT'):
        print (elem.text) #Prints the "Logged in" message.
 
#def checkScan(s, scanRef):

def checkScan(s):
    #
    #---Check Scans---
    #
    # Checks the status of our scan.
    #
    payload = {
               'action':'list',
               'state':'Finished' # parameters are case-sensitive
               }
    r = s.post('https://qualysapi.qg2.apps.qualys.com/api/2.0/fo/scan/', data=payload)
 
    # parse the response.
    print (r.text + " =========================\n")
    xmlreturn = ET.fromstring(r.text)

    
    for elem in xmlreturn.findall('.//SCAN'):
        scanID     = elem[0].text 
        scanName   = elem[1].text
        scanStatus = elem[7].text
        print ("Scan ID: "+scanID + " | Scan Name:" + scanName +" | Status:"+ scanStatus) 
    #return status
  
def checkUnixAuthRecord(s):
    #
    # --- Download details on Unix Authentication Records ---
    #

    payload = {
               'action':'list',
               'details':'All'
              }

    r = s.post('https://qualysapi.qg2.apps.qualys.com/api/2.0/fo/auth/unix/', data=payload)
    
#    print (r.text)
    xmlreturn = ET.fromstring(r.text)

    for elem in xmlreturn.findall('.//AUTH_UNIX'):
        scanID     = elem[0].text 
        scanName   = elem[1].text
        print ("Scan ID: "+scanID + " | Scan Name:" + scanName)
        for elem2 in xmlreturn.findall('.//IP_SET'):
            print (elem2[0].text + " | " + elem2[1].text)

def downloadReport(s, reportID):
    #
    #---Download Report---
    #
    # Lets get the report.
    #
    payload = {
               'action':'fetch',
               'id':reportID,
               }
    r = s.post('https://qualysapi.qg2.apps.qualys.com/api/2.0/fo/report/', data=payload)
 
    # Now that all the hard work was done, lets get that report.
    # No chunking needed due to small size of a single IP scan report.
    with open("/home/tanveer/Scan_Report1"+".pdf", "wb") as report:
        report.write(r.content)

 
def logout(s):
    #

    # ---Logout---
    #
    # Really, you need a description for what this does?
    #
    payload = {
               'action':'logout'
               }
    r = s.post('https://qualysapi.qg2.apps.qualys.com/api/2.0/fo/session/', data=payload)
 
    # Now that all the hard work was done, lets parse the response.
    xmlreturn = ET.fromstring(r.text)
    for elem in xmlreturn.findall('.//TEXT'):
        print (elem.text)   #Prints the "Logged out" message. Not really needed, but reassuring.
 
 
def main():
    s = requests.Session()
    s.headers.update({'X-Requested-With':'Facklers PyQual python primer'})
    login(s)
     # Ok, now lets check on the scan.
    #while checkScan(s) != "Finished":
    #    time.sleep(600)

#    checkUnixAuthRecord(s)

#    checkScan(s)
    downloadReport(s,2968571) 
    logout(s)
    s.close()

if __name__ == "__main__": 
    main()
