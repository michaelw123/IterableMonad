from monad.IterableMonad import TupleMonad

def f(a:int):
    return TupleMonad((a-1, a, a+1))
def g(a:int) :
    return TupleMonad((a, -a))
# left identity
a=2
lhs = TupleMonad((a,)).flatMap(f)
rhs = f(a)
print(lhs == rhs)

# right identity
lhs=TupleMonad((a,)).flatMap(lambda x: TupleMonad((x,)))
rhs=TupleMonad((a,))
print(lhs == rhs)

# associativity
m = TupleMonad((1, 2))
lhs = m.flatMap(f).flatMap(g)
rhs = m.flatMap(lambda x: f(x).flatMap(g))
print(lhs == rhs)

