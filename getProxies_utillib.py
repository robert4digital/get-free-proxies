# Get proxies as list using utillib

# based on
# https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/
# https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/

from lxml.html import fromstring
from bs4 import BeautifulSoup as b
import urllib.request as urllib

def get_proxies():
    site = 'https://free-proxy-list.net/'
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.Request(site,headers=hdr) #sending requests with headers
    url = urllib.urlopen(req).read() #opening and reading the source code
    html = b(url,"lxml")                #structuring the source code in proper format
    rows = html.findAll("tr")       #finding all rows in the table if any.
    proxies = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text for ele in cols]
        try:
            ipaddr = cols[0]        #ipAddress which presents in the first element of cols list
            portNum = cols[1]       #portNum which presents in the second element of cols list
            proxy = ipaddr+":"+portNum  #concatinating both ip and port
            portName = cols[6]          #portName variable result will be yes / No
            if portName == "no":
                pass # proxies.append(str(proxy)) #if yes then it appends the proxy with https
            else:
                # use specific ports only if you have port filters in your organisation
                #if portNum=='80' or portNum=='8080':
                proxies.append(str(proxy)) #if no then it appends the proxy with http
        except:
            pass
    return proxies

###################################################

if __name__ == "__main__":
    print('Number of proxies:',len(get_proxies()))
    print(get_proxies())


