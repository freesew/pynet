from ciscoconfparse import CiscoConfParse
parse=CiscoConfParse("cisco_ipsec.txt")
ccp_find=parse.find_objects(r"^crypto map CRYPTO")
print 'Objects starting with "crypto map CRYPTO" and their children:'
for i in ccp_find:
    print i.text
    for j in i.children:
        print '    ',j.text

print "crypto maps using pfs group2:"
ccp_find=parse.find_objects_w_child(parentspec=r"^crypto map CRYPTO",childspec=r"pfs\s+group2")
for i in ccp_find:
    print i.text
    for j in i.children:  
        print '    ',j.text
print "crypto maps not using AES:"
ccp_find=parse.find_objects_wo_child(parentspec=r"^crypto map CRYPTO",childspec=r"AES-")
for i in ccp_find:
    print i.text
    for j in i.children:
        print '    ',j.text

