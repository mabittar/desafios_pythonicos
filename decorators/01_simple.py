def new_decorator(func, *args, **kwargs):
    def wrap_func():
        print("Code here, before executing the func")
        func(*args, **kwargs)
        print("Code here will execute after the func()")
    return wrap_func


def greetings(name: str):
    print(f"Hello {name}")
    
    
if __name__ == "__main__":
    # calling the function directly
    greetings = new_decorator(greetings, "John")
    greetings()
    # instead of calling the function directly, we pass it to the decorator
    @new_decorator
    def greetings(name: str):
        print(f"Hello {name}")
    
    