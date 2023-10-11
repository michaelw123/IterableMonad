from monad.IterableMonad import ListMonad, TupleMonad

def f(a:int):
    return ListMonad([a-1, a, a+1])


def g(a:int) :
    return ListMonad([a, -a])

#left identity
a = 2
lhs = ListMonad([a]).flatMap(f)
rhs = f(a)
print(lhs == rhs)
# right identity
lhs=ListMonad([a]).flatMap(lambda x: ListMonad([x]))
rhs=ListMonad([a])
print(lhs == rhs)
# associativity
m = ListMonad([1, 2])
lhs = m.flatMap(f).flatMap(g)
rhs = m.flatMap(lambda x: f(x).flatMap(g))
print(lhs == rhs)



'''
# Set
x = SetMonad(set([1,2,2,3]))
y = x.flatMap(lambda a: SetMonad(set([a, a+1]))).flatMap(lambda a: SetMonad(set([a, a*a])))
print(y.value)

# Dict
x = {'a':1, 'b':2, 'c':3, 'd':4}
print(DictMonad(x).flatMap(lambda key: DictMonad({key: x[key]+1})).value)
'''
