import time
import hashlib
from urllib.request import urlopen, Request

url = Request('https://www.facebook.com/groups/2862843204010652')

response = urlopen(url).read()

currentHash = hashlib.sha224()
print("running")
time.sleep(5)
while True:
    try:
        response = urlopen(url).read()

        currentHash = hashlib.sha224(response).hexdigest()

        time.sleep(10)

        response = urlopen(url).read()

        newHash = hashlib.sha224(response).hexdigest()

        if newHash == currentHash:
            continue

        else:
            print("Something Changed")

            response = urlopen(url).read()

            currentHash = hashlib.sha224(response).hexdigest()

            time.sleep(30)

            continue
    except Exception as e:
        print("Error")
