from monad.IterableMonad import DictMonad

def f(d):
    return DictMonad( {k: v+1 for k, v in d.items()})

def g(d):
    return DictMonad( {k: -v for k, v in d.items()})
#left identity
d = {'a': 1, 'b':2}
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