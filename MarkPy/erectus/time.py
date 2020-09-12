## TIME
from time import gmtime, strftime, time_ns


# Now
now = lambda : gmtime()

# Time Now Formatted
time = lambda : strftime('%Y.%m.%d.%H:%M:%S', now())

# Time clock
clock =  lambda : strftime('%H:%M:%S', now())
