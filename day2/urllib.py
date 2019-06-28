import urllib.request
groundctrl = urllib.request.urlopen(majortom)
#Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'
# call the webservice
groundcltr = urllib.request.urlopen(majortom)
# Put fileobject into helmet                                                   
helmet = groundctrl.read()                                                     
# Decode json to python data structure                                         
helmetson = json.loads(helmet.decode('utf-8'))                                 
# Display our pythonic data                                                    
print("\n\nConverted Python Data")                                             
print(helmetson)                                                               
print("\n\nPeople in Space: ", helmetson['number'])                            
people = helmetson['people']                                                   
print(people)

for person in people;
    #print name on the craft
    print(f"{person['name']} is on the {person['craft']}")

