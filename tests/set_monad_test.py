from monad.IterableMonad import SetMonad

f = lambda a: SetMonad({a-1, a, a+1})
g = lambda a: SetMonad({a, a-1})

#left identity
a = 2
lhs = SetMonad({a}).flat_map(f)
rhs = f(a)
print(lhs == rhs)

# right identity
lhs=SetMonad({a}).flat_map(lambda x: SetMonad({x}))
rhs=SetMonad({a})
print(lhs == rhs)

# associativity
m = SetMonad([1, 2])
lhs = m.flat_map(f).flat_map(g)
rhs = m.flat_map(lambda x: f(x).flat_map(g))
print(lhs == rhs)