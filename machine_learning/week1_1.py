import numpy as np
import pylab as pl

x = []
y = []
graph_y = []
graph_x = []
n = 0
a = 0
b = 0
start_point = 0
end_point = 0
gap_point = 0

def output():
    pl.plot(graph_x, graph_y)
    pl.show()

def function_j(update_a, update_b):
    global a, b
    a = update_a
    b = update_b

def function_h(point):
    global x, a, b
    return a * x[point] + b

def calculate():
    global n, y
    sum_ = 0.0
    for i in range(n):
        sum_ = sum_ + pow(function_h(i) - y[i], 2)
        print '#' + str(i) + ' ' + str(function_h(i)) + ' ' + str(y[i])
    print 'result ' + str(sum_)
    return sum_ / (2 * n)

def process():
    global start_point, end_point, gap_point, graph_x, graph_y
    i = start_point
    while i <= end_point:
        print 'test case ' + str(i)
        graph_x.append(i)
        function_j(i, 0)
        graph_y.append(calculate())
        i += gap_point
    print graph_x
    print graph_y

def set_test(s, e, g):
    global start_point, end_point, gap_point
    start_point = s
    end_point = e
    gap_point = g

def set_data(target_x, target_y):
    global x, y, n
    x = target_x
    y = target_y
    if len(x) != len(y):
        print 'data size error'
    else :
        n = len(x)
        print 'data size '+str(n)

set_data([1,2,3], [1,2,3])
set_test(0.0, 2.0, 0.5)
process()
output()
