import requests

response = requests.get("https://httpbin.org/get")
print(response.content)
print(response.text)
print(f"Date time - {type(response.text)}")
print(f"Date time - {type(response.content)}")
