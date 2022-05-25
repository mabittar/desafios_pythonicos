registry = []

def register(func):
    print(f"running func {func}")
    registry.append(func)
    return func

@register
def f1():
    print("f1()")
    
@register
def f2():
    print("f2()")
    
    
def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    
if __name__ == "__main__":
    """
    observe que o módulo register será executado duas vezes
    antes da execução da função main()
    """
    main()