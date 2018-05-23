#!/usr/bin/env python3

while (True): 

  print('what is your netowrk protocol?: ')
  protocol = input()

  if protocol == 'eth' :
    print('ethernet protocol allowed')
    break

  elif protocol == 'fc' :
    print('fiber channel NOT allowed')
    break

  elif protocol == 'ifb' :
    print('infiniband NOT allowed')
    break

  elif protocol == 'otn' :
    print('Optical Network allowed')
    break

  else:
    print('No idea what that technology is')
    break