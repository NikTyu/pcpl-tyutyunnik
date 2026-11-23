from functools import wraps


def print_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if isinstance(result, list):
            for item in result:
                print(item)
        elif isinstance(result, dict):
            for key, value in result.items():
                print(f"{key} = {value}")
        else:
            print(result)
        return result

    return wrapper


if __name__ == "__main__":
    @print_result
    def demo(value):
        return value

    for example in (1, "iu5", {"a": 1, "b": 2}, [1, 2]):
        demo(example)
