from collections.abc import Callable

class IterableMonad:
    def flat_map(self, f:  Callable) -> 'IterableMonad':
            return self.map(f).flatten()
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self == other


class ListMonad(list, IterableMonad):
    def map(self, f:Callable):
        return ListMonad((list)(map(f, self)))
    def flatten(self):
        return ListMonad(list([item for monad in self for item in monad]))

class TupleMonad(tuple, IterableMonad):
    def  map(self, f:Callable):
        return TupleMonad((tuple)(map(f, self)))
    def flatten(self):
        return TupleMonad(tuple([item for monad in self for item in monad]))

class SetMonad(set, IterableMonad):
    def flat_map(self, f: Callable) -> 'IterableMonad':
        return SetMonad([item for monad in map(f, self) for item in monad])

class DictMonad(dict, IterableMonad):
    def map(self, f:Callable):
        return DictMonad({k:f({k:v}) for k, v in self.items()})
    def flatten(self):
        return DictMonad({k: v for k,x  in self.items() for _, v in x.items()})


