#!/usr/bin/env python3

def shorun_sw():

    from napalm import get_network_driver   # Import driver information

    driver = get_network_driver('eos')

    sw = input('Enter desired sw number: ')    # Input to specifiy desired Switch

    if sw == '1' :    # information for Switch 1
    
        sw1 = driver('172.16.2.10', 'admin', 'alta3')

        sw1.open()

        print(sw1.get_config())

    elif sw == '2' :    # information for Switch 2

        sw2 = driver('172.16.2.20', 'admin', 'alta3')

        sw2.open()

        print(sw2.get_config())

    else:    # If non specified input is entered

        print('Please enter valid sw number')

shorun_sw()