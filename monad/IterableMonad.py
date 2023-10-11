from collections.abc import Callable

class IterableMonad:
    def __init__(self, value: object = None):
        iter_op = getattr(value, "__iter__", None)
        if not callable(iter_op):
            self.value = None
        else:
            self.value = value
    def flatMap(self, f:  Callable) -> 'IterableMonad':
        try:
            return self.map(f).flatten()
        except:
            return IterableMonad(None)
    def __eq__(self, other):
        return  self.value == other.value


class ListMonad(IterableMonad):
    def  map(self, f:Callable):
        return ListMonad((list)(map(f, self.value)))
    def flatten(self):
        return ListMonad(list([item for monad in self.value for item in monad.value]))
class TupleMonad(IterableMonad):
    def  map(self, f:Callable):
        return TupleMonad((tuple)(map(f, self.value)))
    def flatten(self):
        return TupleMonad(tuple([item for monad in self.value for item in monad.value]))
class SetMonad(IterableMonad):
    def  map(self, f:Callable):
        return SetMonad((list)(map(f, self.value)))
    def flatten(self):
        return SetMonad(set([item for monad in self.value for item in monad.value]))
class DictMonad(IterableMonad):
    def  map(self, f:Callable):
        return DictMonad([f({k:v}) for k, v in self.value.items()])
    def flatten(self):
        return DictMonad({k: v for monad in self.value for k, v in monad.value.items()})

'''def list_upper(s:str) -> ListMonad:
    return ListMonad([s, s.upper()])
# List
x = 'abc'
y=ListMonad([x])
z = y.flatMap(lambda a: ListMonad([a, a.upper()]))
print(z.value)
#left identity
assert y.flatMap(lambda a: ListMonad([a, a.upper()])).value == list_upper(x).value


# Tuple
x = TupleMonad((1,2,3))
y = x.flatMap(lambda a: TupleMonad((a,a))).flatMap(lambda a: TupleMonad((a*a,a*a)))
print(y.value)

# Set
x = SetMonad(set([1,2,2,3]))
y = x.flatMap(lambda a: SetMonad(set([a, a+1]))).flatMap(lambda a: SetMonad(set([a, a*a])))
print(y.value)

# Dict
x = {'a':1, 'b':2, 'c':3, 'd':4}
print(DictMonad(x).flatMap(lambda key: DictMonad({key: x[key]+1})).value)
'''