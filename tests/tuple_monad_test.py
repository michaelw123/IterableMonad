from monad.IterableMonad import TupleMonad


f = lambda a: TupleMonad((a-1, a, a+1))
g = lambda a: TupleMonad((a, -a))
# left identity
a = 2
lhs = TupleMonad((a,)).flat_map(f)
rhs = f(a)
print(lhs == rhs)

# right identity
lhs=TupleMonad((a,)).flat_map(lambda x: TupleMonad((x,)))
rhs=TupleMonad((a,))
print(lhs == rhs)

# associativity
m = TupleMonad((1, 2))
lhs = m.flat_map(f).flat_map(g)
rhs = m.flat_map(lambda x: f(x).flat_map(g))
print(lhs == rhs)

