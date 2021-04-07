import json
x = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
        },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
        },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
        }
}
f = open('Json.json', 'w')
json.dump(x, f)
f = open('Json.json')
x = json.load(f)
print(x)