import contextlib
from typing import Callable, Dict, Any
from typing import ContextVar
from contextvars import ContextVar

class lisp_manager():
    ctx: ContextVar[dict] = ContextVar("ctx", default={})
    operators: Dict[str, Callable] = {
        "+" : __add__
    }
    @contextmanager
    def lisp():
        print('true')
        #everything below in in __exit__
        try: yield
        catch():

        
        context.reset(token)


    def define_operators(cls, operators: Dict[str, Callable]):
        yield   
    def __add__():


with lisp_manager.lisp():
    print(+ 1 2)