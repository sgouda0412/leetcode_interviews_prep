from typing import list, dict

name: str = "Santosh"
age: int = 29
assets: list = []
posts: tuple = ()
hobbies: dict = {}
is_good: bool = True


posts: list[str] = ["Python Type Hints", "Python Tricks"]
posts: dict[int, str] = {1: "Python Type Hints", 2: "Python Tricks"}


from typing import Final

DATABASE: Final = "MySQL"

from typing import Union

data: Union[int, float] = 3.14
# [data: int|float = 3.14]

from typing import Iterable


def my_func(nums: Iterable):
    for n in nums:
        print(n)


from typing import Optional

a: Optional[int] = 123


from typing import Any


def my_func(nums: Any):
    pass


import time
from typing import Callable


def calc_time(func: Callable):
    start = time.time()
    func()
    end = time.time()
    print(f"Execution time: {end - start}s")


calc_time(lambda: sorted("Yang Zhou is writing!"))


PostsType = dict[int, str]

new_posts: PostsType = {1: "Python Type Hints", 2: "Python Tricks"}
old_posts: PostsType = {}


from typing import Literal

weekends: Literal["Saturday", "Sunday"]
weekends = "Saturday"
weekends = "Monday"

from typing import NewType

Flower = NewType("Flower", str)
lily = Flower("Calla Lily")
hib = Flower("Hibiscus")
print(f"Natural Flowers: {lily}, {hib}")

HybridFlower = NewType("HybridFlower", Flower)
stargazer = HybridFlower("Stargazer")
hardy_hib = HybridFlower("Hardy Hibiscus")
print(f"Hybrid Flowers: {stargazer}, {hardy_hib}")


from typing import Generic, TypeVar, TypedDict
from typing_extensions import ParamSpec

from typing import NoReturn


def raise_error() -> NoReturn:
    raise ValueError("This function always raises an error.")


# https://medium.com/@ramanbazhanau/advanced-type-annotations-in-python-part-1-3c9a592e394
# https://medium.com/@ramanbazhanau/advanced-type-annotations-in-python-part-2-58e0b756aede

from typing import Sequence


def first_element(items: Sequence) -> Any:
    return items[0]


from typing import Mapping


def get_value(data: Mapping, key: str) -> Any:
    return data.get(key)


# for no return type
def print_foo() -> None:
    print("Foo")


print_foo()

import pathlib


def read_file(path: pathlib.Path) -> str:
    with open(path, "r") as file:
        return file.read()


print(read_file(pathlib.Path("mypy.ini")))


# --------------------------------------------------------------


from typing import overload


@overload
def add(a: int, b: int) -> int:
    pass


@overload
def add(a: str, b: str) -> str:
    pass


def add(a, b):
    return a + b


def test2(a: int, b: float, c: str) -> bool:
    return True


# a should be an integer
# b should be a float
# c should be a string

# the return value should be a boolean
