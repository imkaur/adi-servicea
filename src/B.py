import logging
import requests
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')
req = requests.get("http://localhost:5001/serviceA")
logging.warning('Received '+ str(req))
