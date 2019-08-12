from MarkPy import Property, time_ns, Profiler

if __name__ == "__main__":

	profiler = Profiler()
	print(profiler.timeit(number=100, code='class Test:\n\tp=Property("P")\n\nP=Test()\nP.p\nP.p=28',setup='from MarkPy import Property'))
