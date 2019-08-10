from MarkPy import Property






if __name__ == "__main__":
	print('Defining Class')
	class PTest:
		def __init__(self, Name='PropertyTest'):
			self.p1 = Property('p1', 1)
			self.p2 = Property('p2', 2)
			self.p3 = Property('p3', 3)

	print('Creating Instance Class')
	pt = PTest()
	print('Printing Class')
	print(pt)
	print('Print p1')
	print(pt.p1)
	print('Assign something to p2')
	pt.p2 = 28
	print('Print p3')
	print(pt.p3)


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
