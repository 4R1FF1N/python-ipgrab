import requests as req  #ipaws

url: str = "https://checkip.amazonaws.com"
request = req.get(url)
ip: str = request.text
print("IP:", ip)
