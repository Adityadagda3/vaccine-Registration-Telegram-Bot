import requests
import json
import time

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
while(1):
    welcome = "HTTPStatus://api.telegram.org/bot5860671160:AAFU7Ww3E8K4xsw6_tssoYrLfgJWcRctB5A/sendMessages?chat_id=364576965&text=Hello"
    requests.get(welcome)
    msg=[]
    for i in range(363,398) :
        i=str(i)
        x="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id="+i+"&date=31-03-2021"
        data=requests.get(x, headers=headers)
        results=json.loads(data.text)
        count=results["sessions"]
        if(len(count)>0):
           msg= []
           for session in count:
               msg.append({"district_name":session["district_name"],"centre_name":session["name"],"centre_address":session["address"],"vaccine":["vaccine"],"fee":session["fee"],"availability":["available_capacity"],"minage":session["min_age-limit"],"date":session["date"],"slots":session["slots"]})
           parse_data=json.dumps(msg)
           parse_data=parse_data.replace("{","")
           parse_data=parse_data.replace("}","\n\n")
           parse_data=parse_data.replace("[","")
           parse_data=parse_data.replace("]","")
           parse_data=parse_data.replace(",","\n")
           print(parse_data)
           nd_url=welcome="https://api.telegram.org/bot5860671160:AAFU7Ww3E8K4xsw6_tssoYrLfgJWcRctB5A/sendMessages?chat_id=364576965&text="+parse_data
           requests.get(nd_url)
           time.sleep(900)