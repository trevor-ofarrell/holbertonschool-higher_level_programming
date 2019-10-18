#!/usr/bin/env python3

import requests as req

resp = req.get("http://158.69.76.135/level0.php")

resp = req.get("http://158.69.76.135/level0.php")
print(resp.status_code)

resp = req.get("http://158.69.76.135/level0.php")
print(resp.status_code)

print(resp.text)
