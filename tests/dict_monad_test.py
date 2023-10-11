from monad.IterableMonad import DictMonad

def f(d):
    return DictMonad( {k: v+1 for k, v in d.items()})

def g(d):
    return DictMonad( {k: -v for k, v in d.items()})
#left identity
d = {'a': 1, 'b':2}
lhs = DictMonad(d).flatMap(f)
rhs = f(d)
print(lhs == rhs)

# right identity
lhs=DictMonad(d).flatMap(lambda x: DictMonad(x))
rhs=DictMonad(d)
print(lhs == rhs)

# associativity
m = DictMonad(d)
lhs = m.flatMap(f).flatMap(g)
rhs = m.flatMap(lambda x: f(x).flatMap(g))
print(lhs == rhs)