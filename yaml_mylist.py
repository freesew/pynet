import yaml
import json
mylist=range(8)
mylist.append('hello')
mylist.append({})
mylist[-1]={'left':1,'right':2}
print 'python: ',mylist
print 'yaml: '
print yaml.dump(mylist,default_flow_style=False)
print 'json: '
print json.dumps(mylist)
with open("yamlout.yml","w") as f:
    f.write(yaml.dump(mylist,default_flow_style=False))
with open("jsonout.json","w") as f:
    json.dump(mylist,f)
