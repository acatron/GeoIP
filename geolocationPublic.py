import urllib.request
import json
import urllib.parse

#ip = input("Please enter your user IP: ")
#the query above is for testing user input

#event['ip_list'] = ['50.50.50.50', '100.100.100.100', '200.200.200.200']
#example list of what was asked

listOfIPs =['99.226.238.79', '173.53.70.42', '186.7.143.101']

nonUSIPList = []
nonUSCountryList = []

eventlist = []
#contains final list of IPs


#print(ip)

def lambda_handler(event):


#  event[ip_list] = ['99.226.238.79', '173.53.70.42', '186.7.143.101']
  #the query above is for testing lists
  
  #ip = event['addIP']
  #the query above is for testing in the client space in the API Gateway
  

#  ip = event['ip']
#Code above is for testing single IP in AWS Lambda UI
  for ip in listOfIPs:
    event = ip.strip()
    eventlist.append(event)
    #ip.append(event)
    #print(ip); 
#  for ip in event:
#    event = 'ip'; 
#Code above is for testing list of strings in AWS Lambda UI  
  
  #ip = initIPList[]

    with urllib.request.urlopen("https://freegeoip.app/json/" + event) as f:
      data = json.loads(f.read())

    if (data['country_name'] != "United States") :
      if (data['ip'] not in nonUSIPList) :
        nonUSIPList.append(data['ip'])
        nonUSCountryList.append(data['country_name'])
    
    print('Your IP is ' + data['ip'])
    print('Your city is ' + data['city'])
    print('Your state is ' + data['region_name'])
    print('Your country is ' + data['country_name'])
    print('')



    
  stringOfIPs = ' '.join(nonUSIPList)
  stringOfCountries = ' '.join(nonUSCountryList)

    
    #webhook=event['webhook']
    #data=webhook
  url = ' YOUR WEBHOOK URL'
  data = {
      'text' : "The IPs are: \n" + stringOfIPs + " \n" + "The countries are : \n" + stringOfCountries
  }
  data = json.dumps(data).encode('utf-8') #working
    #data = json.dumps({'text': "listOfIPs"}).encode('utf-8') #data needs to be in bytes
    #data = json.dumps({listOfIPs}).encode('utf-8')
  headers = {'Content-Type': 'application/json'}
  req = urllib.request.Request(url, data, headers)
  resp = urllib.request.urlopen(req)

  print('This is the list of all IPs that were iterated through')
  print(*eventlist)
  print('')
  print('This is the non-US IP list')
  print(*nonUSIPList)
  print('This is the non-US country list')
  print(*nonUSCountryList)

 # response = resp.read()

lambda_handler(listOfIPs)
#print (*listOfIPs)
