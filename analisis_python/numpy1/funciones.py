# coding: utf-8
def simple_operation(val):
    return val * 10
    
a = np.random.randint(1, 10, 10)
a
simple_operation(a[0])
for i in a:
    print(simple_operation(i) )
    
np.vectorize(simple_operation)
func_vec = np.vectorize(simple_operation)
func_vec(a)
a
func_vec(a)
b = func_vec(a)
b
