
class My:
    def __init__(self) -> None:
        pass

    def __call__(self, *args, **kwargs):
        return f'--->'

first = My()

print(first)
print(first())

