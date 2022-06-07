import numpy

a = numpy.arange(15)
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.dtype.name)
rng = numpy.random.default_rng(20)
k = rng.integers(5, size =(2,4))
print(k)

print(numpy.unique(k))