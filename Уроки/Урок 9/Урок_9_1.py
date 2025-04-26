# import urllib.request

# opener = urllib.request.build_opener()
# response = opener.open("https://httpbin.org/get")
# print(response.read())

import requests

# response = requests.get("https://httpbin.org/get")
# print(response.content)
# print(type(response.content))

response = requests.post("https://httpbin.org/get", data="Test data", headers={"h1": "Test title"})
print(response.text)