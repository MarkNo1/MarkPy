from MarkPy import Property, time_ns


if __name__ == "__main__":
	print('Defining Class')

	class PTest:
		p1 = Property('P1')
		p2 = Property('P2')


	print('Creating Instance Class')
	pt = PTest()


### OUTPUT #################################################
# (base) C:\Users\mark\WorkingSpace\MarkPy>python testLib.py
# Property - Ini
# Logger - Ini
# File - Ini
# File - Ini
# Property - Ini
# Logger - Ini
# File - Ini
# File - Ini
# Defining Class
# Printing Class
# <__main__.C object at 0x000002D2A49F8128>
# Print a
# Property - Get
# State - Ini
# Logger - Del
# File - Del
# File - Del
# 1
# Assign something to b
# Property - Set
# State - Ini
# Logger - Del
# File - Del
# File - Del
# Print b
# Property - Get
# State - Ini
# State - Del
# 2
# Property - Del
# State - Del
# Property - Del
# State - Del
