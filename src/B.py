import logging
import requests
req = requests.get("http://localhost:5001/serviceA")
print(req)
print(req.content)
log.setLevel(logging.DEBUG)
