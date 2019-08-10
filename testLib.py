from MarkPy import Property, time_ns, Profiler

if __name__ == "__main__":

	profiler = Profiler()
	print(profiler.timeit(number=1, code='class Test:\n\tp=Property("P")\n\nP=Test()',setup='from MarkPy import Property'))
