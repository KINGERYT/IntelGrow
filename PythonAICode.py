from bs4 import BeautifulSoup
import requests
import serial
import json
try:
  while True:
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    port=serial.Serial(port='COM5', baudrate=9600, timeout=.1)
    def weather(city):
       global location,time,info,tempc,temp
       city=city.replace(" ","+")
       res=requests.get(f'https://www.google.com/search?q={city}&oq={city}'f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid='f'chrome&ie=UTF-8',headers=headers)
       print("\n")
       soup=BeautifulSoup(res.text,'html.parser')
       location=soup.select('#wob_loc')[0].getText().strip()
       time=soup.select('#wob_dts')[0].getText().strip()
       info=soup.select('#wob_dc')[0].getText().strip()
       temp=soup.select('#wob_tm')[0].getText().strip()
       print(location)
       print(time)
       print(info)
       print(f"{temp}°C")
    print("city name")
    city=input()
    city=city+" weather"
    weather(city)
    if "rainy" in info.lower() or "foggy" in info.lower()or "cloudy" in info.lower()or "haze" in info.lower():
      port.write(b'b')
    elif "sunny" in info.lower() or "windy" in info.lower():
      port.write(b'd')

except:
  print("Port Disconnected....")
