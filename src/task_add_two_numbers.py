from task_base import TaskBase


class AddTwoNumbers(TaskBase):
    name = "add_two_numbers"

    def run(self, a:int, b:int) -> None:
        print(a + b)
        return