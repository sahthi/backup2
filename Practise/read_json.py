#!/usr/bin/python3

import requests as req

resp = req.get("http://192.168.2.129/send_json.php")
print(resp.json())

