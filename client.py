import requests
import random

def generateQuotes():
  with open("static/quotes.txt", encoding="utf8") as f:
    line = next(f)
    for num, aline in enumerate(f,2):
      if random.randrange(num):
        if line.startswith('--'):
          line = line[3:]
        elif line.startswith('\n'):
          line = next(f)
          continue
      line = aline
    return line

url = 'http://127.0.0.1:5000/post'

while True:
  n = 0
  with open("templates/quantity.txt", encoding="utf8") as f:
    n = f.read()
    if n != "":
      n = int(n)
    else:
      n = 0
  with open('templates/quantity.txt','w'):
    pass
  while n > 0:
    payload = {'quote': "1"}
    r = requests.post(url, json=payload)
    print(r.text)
    print(r.status_code)
    n -= 1

