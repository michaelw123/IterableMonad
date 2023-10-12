from monad.IterableMonad import ListMonad, TupleMonad

def f(a:int):
    return ListMonad([a-1, a, a+1])


def g(a:int) :
    return ListMonad([a, -a])

#left identity
a = 2
lhs = ListMonad([a]).flat_map(f)
rhs = f(a)
print(lhs == rhs)
# right identity
lhs=ListMonad([a]).flat_map(lambda x: ListMonad([x]))
rhs=ListMonad([a])
print(lhs == rhs)
# associativity
m = ListMonad([1, 2])
lhs = m.flat_map(f).flat_map(g)
rhs = m.flat_map(lambda x: f(x).flat_map(g))
print(lhs == rhs)


