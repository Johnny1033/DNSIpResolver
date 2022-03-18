import dns.resolver

#change these to reflect what domains you want to find the DNS IP
domains = ['espn.com', 'google.com', 'reddit.com']
names = ['espn.com', 'google.com', 'reddit.com']

things = []

def getIps(names):
    for name in names: 
        global things
        for qtype in 'A':
            test = dns.resolver.resolve(name, qtype, raise_on_no_answer=False)
            things += test
            print('test', test)
            print('getIps', things)

#def formatIp(things):
    #for thing in things:
        #print(thing.replace('<DNS IN A rdata: '))
        #names += thing

getIps(names)
#formatIp(things)
#print(things)
