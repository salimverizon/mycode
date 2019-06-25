#!/usr/bin/env python3

hosts = [{"server" : "north" , "ip" : "10.1.2.3"}, {"server" : "south" , "ip" : "10.4.5.6"}, {"server" : "west" , "ip" : "10.7.8.9"}]
new = {"server" : "est" , "ip" : "10.10.11.12"}
hosts.append(new)
print(hosts[0]["server"], hosts[0]["ip"])
print(hosts[1]["server"], hosts[1]["ip"])
print(hosts[2]["server"], hosts[2]["ip"])
print(hosts[3]["server"], hosts[3]["ip"])
