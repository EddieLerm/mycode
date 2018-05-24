#!/usr/bin/env python3

round = 0

while(True):

    print('What is the IPv4 address used to broadcast on a local network? ')
    answer = input()
    round = round + 1

    if (answer == '255.255.255.255'):
        print('Correct!')
        break             
    elif (round == 3):
        print('Sorry, the answer was 255.255.255.255')
        break             
    else:
        print('Sorry. Try again!')
