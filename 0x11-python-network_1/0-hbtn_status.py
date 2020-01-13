#usr/bin/python3
#script that fetches https://intranet.hbtn.io/status
import urllib3
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
   html = response.read()
