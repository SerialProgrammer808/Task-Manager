from task_class import Task
from check_date import check_date
import pytest

def main():
    test_task()
    test_check_date()

def test_task():
    task = Task("Math homework", "01/08")
    assert str(task) == "Math homework due 01/08"
    assert task.information == "Math homework"
    assert task.date == "01/08"

def test_check_date():
    assert(check_date("01/32")) == False
    assert(check_date("13/01")) == False
    assert(check_date("1/9")) == False
    assert(check_date("02/30")) == False
    assert(check_date("01/31")) == True

if __name__ == "__main__":
    main()


