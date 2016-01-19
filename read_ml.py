import yaml
import json
import pprint

pp=pprint.PrettyPrinter(indent=4)

with open("yamlout.yml","r") as f:
    y=yaml.load(f.read())
print 'yaml read: '
pp.pprint(y)

with open("jsonout.json","r") as f:
    j=json.load(f)

print 'json read: '
pp.pprint(j)

