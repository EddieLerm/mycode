#!/usr/bin/env python3
import os
import sys 
from blessings import Terminal
t = Terminal()
print(t.clear())

def close(event):
    master.withdraw()
    sys.exit()

def yellow_wp(p):
   print(t.clear_bol,t.bold_black_on_yellow(p))

def trx(p):
    x = t.width - len(p)-1
    return int(x)

def top_right(p):
    with t.location(trx(p), 0): 
        yellow_wp(p)

def prompt_location():
    return t.location(0,t.height-2)

def response_location(p):
    return t.location(len(p) + 1,t.height-2)

def prompt(p):
    with prompt_location():
       p = p + " (q + Enter to quit):"
       print(t.reverse(p),t.clear_eol)
    with response_location(p):
       orders = input()
    return orders   

orders = ""
while orders != 'q': 
    orders = prompt("Your orders")
    orders
    top_right(orders)
    if orders[:3]=='mtr':
      with t.location(0,3):
         os.system(orders)

yellow_wp("Thanks for all the fish")