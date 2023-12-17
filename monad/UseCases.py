#Parameter Checking for varg
from IterableMonad import ListMonad


'''def list_pipeline():
    list_monad = ListMonad([1,2,3,4])
    result = (list_monad.map(lambda x: x+1)
              .flat_map(lambda x: ListMonad([x+1, x-1]))
              .flat_map(lambda x: ListMonad([str(x)])))
    print(result.value)


list_pipeline()'''

for x in {1:"a",2:"b",3:"c"}:
    print(x)
