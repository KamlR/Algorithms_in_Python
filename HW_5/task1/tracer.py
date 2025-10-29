from functools import wraps

def tracer(func):
    depth = 0 

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal depth
        indent = "  " * depth  
        print(f"{indent}→ Вход: {func.__name__}{args}")
        depth += 1
        result = func(*args, **kwargs)
        depth -= 1
        print(f"{indent}← Выход: {func.__name__}{args} = {result}")
        return result
    return wrapper


@tracer
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


@tracer
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    print("\nТрассировка factorial(4):")
    factorial(4)

    print("\nТрассировка fibonacci(4):")
    fibonacci(4)
