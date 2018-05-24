#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
proto.extend('dns') # this line will add 'dns' to the end of our list
print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list

print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.append(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)
