from collections.abc import Callable

class IterableMonad:
    def __init__(self, value: object = None):
        iter_op = getattr(value, "__iter__", None)
        if not callable(iter_op):
            self.value = None
        else:
            self.value = value
    def flat_map(self, f:  Callable) -> 'IterableMonad':
        try:
            return self.map(f).flatten()
        except:
            return IterableMonad(None)
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.value == other.value


class ListMonad(IterableMonad):
    def map(self, f:Callable):
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
