#!/usr/bin/env python3
try: # code we want to try to run goes under the try
    print("This is what we try to do, but we can raise an error...")
    input()
    raise SystemError
except ZeroDivisionError:  # Only catches div by zero errors
    print("Computers do not like div by zero")
except SystemError:
    print("Malfunction will now self destruct") 
except IOError:
    print("This code raised an IO error")
except:
    print("We're sorry, something unexpected happened. See your IT department.")
