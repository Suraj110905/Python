import numpy
ages=[5,2,6,3,4,2,5,7,8,9,5,1,2,3,5,5,6,8,5,2,6,3,4,8,5]
x=numpy.percentile(ages,5)
print(x)


#what is the age that 90% of the people are younger than
import numpy
ages=[65,52,6,45]
x=numpy.percentile(ages,90)
print(x)