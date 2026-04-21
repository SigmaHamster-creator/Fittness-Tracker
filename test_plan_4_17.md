# Testing Plan

## Overview
**Functions tested:**  
**Testing types:** Unit / Integration / Regression  
**Date:**  

---

## Test Case Table

| Test ID | Description | Input(s) | Expected Output | Type | Pass/Fail |  Notes  |
|---------|-------------|----------|-----------------|------|-----------|---------|
|  01.    |Testprintlist|push,abc,1|Name: push, Description: abc, Time Spent: 1 minute | edge ||Steven|
|  02.    |Test reading a empty file|"","",""|"time: , description: "|edge||Tested by Leon
|  03.    |test add_activity|[],{"name": "jogging", "description":"running slowly for exercise", "time":30}|[{'name': 'jogging', 'description': 'running slowly for exercise', 'time': 30}]|normal case|pass|Tested by Yiming|
|  04.    |test update_activity|["jogging", "0", ""]|[{'name': 'jogging', 'description': '', 'time': 0}]|edge case|Pass||
|  05.    |test delete_activity|{'name': 'jogging', 'description': 'running slowly for exercise', 'time': 30},"run"|"Can not found activity run"|error case|Pass||
|  06.    |test create_activity|push, 12 reps, 10|"name": "push", "description":"12 reps", "time":10|normal case|Pass|Tested by Danny|
|  07.    |test change_time|100|Invalid number, please try again!|error case|Fail|Tested by Danny|
## Code Used for Testing

```python
def display_list(list_activities):
    if len(list_activities) == 0:
        print("No activities yet")
    else:
        for i in range(len(list_activities)):
            activity = list_activities[i]
            print(f"{i+1}. Name: {activity['name']} | Description: {activity['description']} | Time: {activity['time']} Minutes")
def read_data(): #Leon
    list_activities = []
    try:
        with open("Data.txt", "r") as f:
            for line in f:
                name, time, description = line.strip().split(",")
                activity = {
                    "name": name,
                    "time": int(time),
                    "description": description
                }
                list_activities.append(activity)
    except FileNotFoundError:
        pass
    return list_activities
def create_activity(name, description, time):
        activity = {
        "name" : name,
        "description" : description,
        "time" : time 
    }
    return activity
def update_activity(list_activities):
    update_input = input("Enter name of activity you want to update: ")
    found = False
    for a in list_activities:
        if a["name"] == update_input:
            new_time = int(input("Enter new time you want to update: "))
            new_description = input("Enter new description you want to update: ")
            a["time"] = new_time
            a["description"] = new_description
            print("Activity updated!")
            found = True
            break
    if not found:
        print("Activity not found!")
def delete_activity(list_activities):
    remove_input = input("Enter the name of activity that you want to remove: ")
    found = False
    for a in list_activities:
        if a["name"] == remove_input:
            list_activities.remove(a)
            print("Activity removed!")
            found = True
            break
    if not found:
        print(f"Can not found activity {remove_input}")
def add_activity(list_activities, activity):
    list_activities.append(activity)
    print("Activity added!")
    return list_activities
def change_time(list_activities):
    if len(list_activities) == 0:
        print("No activities to update yet!")
        return
    
    display_list(list_activities)
    choice_update = int(input("Select activity number you want to change time: "))

    if choice_update >= 1 and choice_update <= len(list_activities):
        new_time = int(input("Enter new time for your activity here: "))
        list_activities[choice_update - 1]["time"] = new_time
        print("Time changed!") 
    else: 
        print("Invalid number, please try again!")
