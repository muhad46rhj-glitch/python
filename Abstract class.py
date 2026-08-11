from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self,x):
        print(f"passed value: {x}")

    @abstractmethod
    def task(self):
        print("we are inside absclass task")

class test_class(Absclass):
    def task(self):
        print("we are inside test_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)