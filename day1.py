import numpy

input = numpy.loadtxt('input/day1.txt',dtype=int)

increased = 0

i=0
for num in input[1:]:
    if num > input[i]:
        increased+=1
    # print(num, input[i], increased)
    i+=1

print("> increased", increased)