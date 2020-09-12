from MarkPy import Property, time_ns, Profiler
import logging

TestCode = \
'''
class TestMarkPy:
	filename = Property("FileName", 'TestMarkPy.Property')
	windows_size = Property("widows size", 'TestMarkPy.Property')
	data = Property('Data', 'TestMarkPy.Property')

testclass = TestMarkPy()
testclass.filename = "FirstTest"
testclass.filename = "FirstTest1"
testclass.filename = "FirstTest2"
testclass.windows_size = (3840,2160)
testclass.data = [1,2,3,4,5,6,7,8,9,10]

testclass.data
testclass.windows_size
testclass.filename
'''


if __name__ == "__main__":
	logging.basicConfig()
	logging.getLogger().setLevel(logging.INFO)
	profiler = Profiler()
	print('Testing code: \n', TestCode)
	print(profiler.timeit(number=1, code=TestCode,setup='from MarkPy import Property'))
