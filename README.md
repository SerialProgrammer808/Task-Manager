# TASK MANAGER PROJECT
## Video Demo:  <https://youtu.be/MqbGOJpUFoE>
## Background
As a person who has a lot on their plate and is forgetful at times, I figured that a perfect final project for this course would be a task management application. This application was created with the intention of showcasing what I learned in CS50's Introduction to Programming with Python and aiding me in keeping track of my tasks as I enter the spring semester with 18 credits!

## Overview
This project utilizes the following:
```
- Python
- Functions
- If-else statements
- Loops
- Trys and exceptions
- Libraries (re, attrgetter, tabulate)
- Unit tests
- File I/O
- Regular expressions
- Object-oriented programming (OOP)
```
The main file of this task management application makes use of a task class that I created (further explained in "The Task Class"), the main function, as well as five helper functions.

The functions I decided to create and utilize for this project were `add_task()`, `delete_task()`, `update_task()`, `display_task()`, `save_task()`.
## Project.py
### Main
Since I have not learned how to implement an advanced user interface using front end development, I have instead chosen the command-line interface as my user's interaction hub.

The main function first creates an empty list called `to_do_list`. This list is purposefully created to be blank each time the program is executed. To ensure that no invalid lists are passed into the functions, the program automatically passes the `to_do_list` into the function, rather than letting the user be in control of that. The main function then takes care of creating this interactive command-line interface by executing an infinite loop and asking for user input. The user's answer is stored in the `command` variable.
####
```python
to_do_list = list()
while True:
    command = input("What would you like to do? (ADD, DELETE, UPDATE, SAVE, DISPLAY, QUIT): ")
```
Then, a block of if statements will validate the user input and execute the corresponding functions (each function is explained in its individual section)
####
```python
    if command.strip().upper() == "ADD":
        print(add_task(to_do_list))
    elif command.strip().upper() == "DELETE":
        print(delete_task(to_do_list))
    elif command.strip().upper() == "UPDATE":
        print(update_task(to_do_list))
    elif command.strip().upper() == "SAVE":
        save_task(to_do_list)
    elif command.strip().upper() == "DISPLAY":
        print(display_task(to_do_list))
    elif command.strip().upper() == "QUIT":
        break
    else:
        print("Invalid command")
```
Due the `while True:` line of code, this program will run indefinitely until the user responds with "Quit". This program is designed like that in order to avoid having to re-run everytime you want to do something with your list of tasks.

### add_task
The `add_task()` function takes a single list an argument and begins by asks for a task description and a date which are stored as separate variables. Those variables are then passed into the `Task` initializer method, which handles the date validation, and appended to the list given in the argument. The function only returns a string, confirming that the task has been added.
####
```python
def add_task(list):
    try:
        info = input("What task would you like to add?: ")
        due_date = input("Due (MM/DD): ")
        list.append(Task(info, due_date))
        return "Task added!"

    except:
        return "invalid date"
```
### delete_task
The `delete_task()` function takes a single list as an argument and begins by asking for the description of the task to delete as well as the date of the task to delete. The funciton asks for both description and the date to ensure the correct task is being deleted due to multiple tasks being able to share the same description or date.

These are then stored as separate variables and are then passed into the `Task` initializer method and stored as `task`. A loop iterates through the objects in the given list and checks if the `str(task)` is equal to `str(object)`. The program must compare the `str` and not the actual `task` and `object` due to the fact that they are stored differently and are not identical to eachother.

If the task is present in the list, the object is `.remove()` and the function returns a string confirming that the task has been deleted. If no identical task is present in the list, the function returns the message `"Invalid task"`
####
```python
def delete_task(list):
    try:
        item = input("What task would you like to delete?: ")
        due_date = input("When is this task due? (MM/DD): ")
        task = Task(item, due_date)
        for object in list:
            if str(task) == str(object):
                list.remove(object)
                return "Task deleted!"
        else:
            return "Invalid task"

    except:
        return "Invalid task"

```
### update_task
The `update_task()` function takes a single list as an argument and uses the same logic as `add_task()` and `delete_task()` put together. If the task that is being updated does not exist in the list, the function returns the message `"Invalid task"`. If all the inputs are valid, the function returns a string confirmtion that the task has been updated.
####
```python
def update_task(task_list):
    try:
        old_item = input("What task would you like to update?: ")
        old_time = input("When is this task due?: ")
        old_task = Task(old_item, old_time)

        for task in task_list:
            if str(old_task) == str(task):
                task_list.remove(task)
                break
        else:
            return "Invalid task"

        new_item = input("What is the new task?: ")
        new_time = input("What is the new time?: ")
        new_task = Task(new_item, new_time)
        task_list.append(new_task)
        return "Task updated!"

    except ValueError:
        return "Invalid date"
```

### display_task
The `display_task()` funciton takes a single list as an arguments, sorts the list by date using the `operator` libary, and uses the `tabulate` library to display the list as a table in the terminal.

Since `tabulate` works best with nested lists and our `to_do_list` doesn't hold any strings, we must convert the given list into a format that can be used by `tabulate`.

We start off by creating an empty list `new_list`, sorting the given list, and creating the headers for the table are created.

We then iterate over the items of the sorted given list and in each iteration we create a "listette" (tiny list), split the contents of `str(item)` storing each as its own `task` and  `due` variable, append `task` and `due` to the listette, and appending the listette to `new_list`. Through this we have effectively reformated the list of objects into a nested list made up of tasks and dates.

we then use `tabulate` to return the table of the `new_list`

####
```python
def display_task(list):
    new_list = []
    list = sorted(list, key=attrgetter("date"))
    headers = ["Task", "Due"]

    for item in list:

        listette = []
        task, due = str(item).split(" due ")
        listette.append(task)
        listette.append(due)
        new_list.append(listette)

    return(tabulate(new_list, headers=headers, tablefmt="fancy_outline"))
```
### save task
The `save_task()` function uses the `display_task()` function but rather than just displaying it in the terminal, the ouput is stored as a `.txt` file.
####
```python
def save_task(list):
    with open("to_do_list.txt", "w") as file:
        file.write(display_task(list))
```
## The Task Class
The `Task()` class was created to standardize what a task is for the purposes of this program.

the `__init__` method takes thtree arguments, self, description, and a date respectively. Since the description can be anything the user wants, the setting of the description is handled directly by `__init__`.
###
```python
from check_date import check_date

class Task():
    def __init__(self, description, date):
        self.description = description
        self.date = date
```
The date however, has more regulations and so a date getter and setter function is created to ensure the given date is put in a specific format. The setter takes self and date as arguements and leaves the validation of the date's format to `check_date` function (further explained in "Date Checking").
###
```python
@property
def date(self):
    return self._date

@date.setter
def date(self, date):
    if check_date(date):
        self._date = date
    else:
        raise ValueError("Invalid date")
```
The last method of the `Task()` class reformats the class object into a `str` that is easier for users to interact with.
###
```python
def __str__(self):
    return f"{self.information} due {self.date}"
```

## Date Checking
The `check_date()` function takes a date as an argument and handles the validation of the dates used to construct the `Task()`s. This function uses a regular expression to ensure that valid dates are in the format "MM/DD" and to ensure that the maximum days in a given month are followed. By using a regular expression, **all** invalid arguments will be filtered out.
###
```python
import re

def check_date(date):
    date_pattern = r'^((0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-8]))$|^((0[13578]|1[02])/(29|30|31))$|^((0[469]|11)/(29|30))$'
    if re.search(date_pattern, date):
        return True
    else:
        return False
```

## Unit Testing
In the unit testing portion of this project, the most important parts to test were the `Task()` class and the `check_date()` function. The pytest library is utilized to ensure that the all the instance methods of `Task()` work and that `check_date()` filters out invalid dates.
###
```python
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
```
## MAHALO
Thank you to David Malan and the CS50 team for your commitment to education! I thoroughly enjoyed this course and I look forward to more learning and creating in the future!

Or as we say in 'ōlelo Hawai'i,
```python
print("Mahalo nui loa iā ʻoukou a pau!")
```
