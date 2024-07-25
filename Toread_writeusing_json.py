import json

# Data to be written
details= {
	"name": "chandana",
	"rollno": 11,
	"cgpa": 7.6,
	"phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(details, indent=4)

# Writing to sample.json
with open("totest.json", "w") as outfile:
	outfile.write(json_object)
with open('totest.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object)
print(type(json_object))