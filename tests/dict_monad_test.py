from monad.IterableMonad import DictMonad


f = lambda a: DictMonad( {k: v+1 for k, v in a.items()})
g = lambda a: DictMonad( {k: -v for k, v in a.items()})
#left identity
d = {'a': 1, 'b':2}
m = DictMonad(d).map(f)
lhs = DictMonad(d).flat_map(f)
rhs = f(d)
print(lhs == rhs)

# right identity
lhs=DictMonad(d).flat_map(lambda x: DictMonad(x))
rhs=DictMonad(d)
print(lhs == rhs)

# associativity
m = DictMonad(d)
lhs = m.flat_map(f).flat_map(g)
rhs = m.flat_map(lambda x: f(x).flat_map(g))
print(lhs == rhs)