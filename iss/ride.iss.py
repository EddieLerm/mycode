import urllib.request
import json
## Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
groundctrl = urllib.request.urlopen(majortom)

## put fileobject into helmet
helmet = groundctrl.read()

## decode json to python data structure
helmeston = json.loads(helmet.decode('utf-8))

## display our pythonic data
print("\n\nConverted python data")
print(helmetson)

print(\n\n"People in Space: ", helmetson['number'])
people = helmetson['people']
print(people)