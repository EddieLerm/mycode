#!/usr/bin/env python3

#list for interface ETH0 config's
my_list= [ "192.168.0.5", 5060, "UP" ]

# Prints the IP add of ETH0
print("The first item in the list (IP): " + my_list[0] )

# Prints the Port number of ETH0
print("The second item in the list (port): " + str(my_list[1]) )

#Prints Status of ETH0
print("The last item in the list (state): " +my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print('When I ssh into IP addresses ' + new_list[3], 'or ' + new_list[4],'I am unable to ping ports ' + str(new_list[0]), ', ' + new_list[1], ', or ' +str(new_list[2]))