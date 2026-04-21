#Automated testing
import io
import sys
import unittest

def your_function_here(param):
    pass #placeholder

def create_activity(name, description, time): #Yiming
    activity = {
        "name" : name,
        "description" : description,
        "time" : time 
    }
    return activity

def display_list(list_activities): #STEVEN
    if len(list_activities) == 0:
        print("No activities yet")
    else:
        for i in range(len(list_activities)):
            activity = list_activities[i]
            pri = f"{i+1}. Name: {activity['name']} | Description: {activity['description']} | Time: {activity['time']} Minutes"
    return pri
def add_activity(list_activities, activity): 
    list_activities.append(activity)
    print("Activity added!")
    return list_activities

def total_time_spent(list_activities): #STEVEN
    total = 0
    for i in list_activities:
        total += int(i["time"])
    return total

def delete_activity(list_activities,_update): # Yiming
        #remove_input = input("Enter the name of activity that you want to remove: ")
        remove_input = _update[0]
        found = False
        for a in list_activities:
            if a["name"] == remove_input:
                list_activities.remove(a)
                print("Activity removed!")
                found = True
                break
        if not found:
            print(f"Can not found activity {remove_input}")

def update_activity(list_activities, _input): # Yiming
    #update_input = input("Enter name of activity you want to update: ")
    update_input = _input[0]
    found = False
    for a in list_activities:
        if a["name"] == update_input:
            #new_time = int(input("Enter new time you want to update: "))
            new_time = int(_input[1])
            #new_description = input("Enter new description you want to update: ")
            new_description = _input[2]
            a["time"] = new_time
            a["description"] = new_description
            print("Activity updated!")
            found = True
            break
    if not found:
        print("Activity not found!")

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

def save_data(list_activities): #Leon
    with open("Data.txt", "w") as f:
        for a in list_activities:
            f.write(f"{a['name']},{a['time']},{a['description']}\n")

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

class TestYourFunction(unittest.TestCase):

    # ADD TESTS HERE
    # NOTE: use self.assertTrue, self.assertFalse or self.assertEqual
    def test_printlist(self):
        output = display_list([{"name": "push","description": "abc","time":1}])
        self.assertEqual(output,'1. Name: push | Description: abc | Time: 1 Minutes')
    def test_add_activity(self):
        self.assertEqual(add_activity([],{"name": "jogging", "description":"running slowly for exercise", "time":30}),[{'name': 'jogging', 'description': 'running slowly for exercise', 'time': 30}])
    def test_update_activity(self):
        list_activities = [{'name': 'jogging', 'description': 'running slowly for exercise', 'time': 30}]
        _input = ["jogging", "0", ""]
        update_activity(list_activities,_input)
        self.assertEqual(list_activities,[{'name': 'jogging', 'description': '', 'time': 0}])
    def test_delete_activity(self):
        list_activities = [{'name': 'jogging', 'description': 'running slowly for exercise', 'time': 30}]
        _input = ["run"]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        delete_activity(list_activities,_input)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output,"Can not found activity run")
    def test_read_empty_file(self): #Leon
        with open("Data.txt", "w") as f:
            f.write("")
        data = read_data()
        self.assertEqual(data, [])
        
if __name__ == '__main__':
    unittest.main()
