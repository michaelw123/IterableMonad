from monad.IterableMonad import SetMonad

def f(a:int):
    return SetMonad({a-1, a, a+1})


def g(a:int) :
    return SetMonad({a, -a})

#left identity
a = 2
lhs = SetMonad({a}).flatMap(f)
rhs = f(a)
print(lhs == rhs)

# right identity
lhs=SetMonad({a}).flatMap(lambda x: SetMonad({x}))
rhs=SetMonad({a})
print(lhs == rhs)

# associativity
m = SetMonad([1, 2])
lhs = m.flatMap(f).flatMap(g)
rhs = m.flatMap(lambda x: f(x).flatMap(g))
print(lhs == rhs)