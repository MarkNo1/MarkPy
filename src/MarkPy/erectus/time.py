## TIME
from time import gmtime, strftime

# Now
now = lambda : gmtime()

# Time Now Formatted
time = lambda : strftime('%Y.%m.%d.%H:%M', now())

# Time clock
clock =  lambda : strftime('%H:%M:%S', now())
