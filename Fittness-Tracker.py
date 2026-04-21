# Allow the user to record a fitness activity with name/description.
# Enter the time spent on the fitness activity (eg. in minutes).
# Allow the user to view a list of all recorded activities.
# Clearly show the time spent for each of the recorded activities.
# Allow the user to change/update the time spent on each activity.
# Save fitness data so it is available when the program is run again.

#FUNCTION
    
def create_activity(name, description, time): #Yiming
    """
    Description:
    Creates a dicionary activity with its details attached.

    Parameters:
    name(str):The name of the activity.
    description(str):The description of the activity.
    time(int):The time used for the activity.

    Returns:
    dict:The activity and its details.

    Raises:
    ValueError: If name is a integer.

    Example:
        >>> create_activity("run","slow run",200)
        activity = {
        "name" : "run",
        "description" : "slow run",
        "time" : 200
    
    """
    activity = {
        "name" : name,
        "description" : description,
        "time" : time 
    }
    return activity

def display_list(list_activities): #STEVEN
    """
    Description:
    Shows the activity(ies) with its detials in a printing format.

    Parameters:
    list_activities(list): a list of activitiy(ies) dictionary(ies).
        
    Returns:
    str:printing message.

    Raises:
    ValueError: if list_activities is a integer.

    Example:
        >>>display_list([{"name" : "run","description" : "slow run","time" : 200 }])
        1. Name: run | Description: slow run | Time: 200 Minutes

    """
    if len(list_activities) == 0:
        print("No activities yet")
    else:
        for i in range(len(list_activities)):
            activity = list_activities[i]
            print(f"{i+1}. Name: {activity['name']} | Description: {activity['description']} | Time: {activity['time']} Minutes")
     
def add_activity(list_activities, activity): 
    """
    Description:
    Adds new activity to the activity list.

    Parameters:
    list_activities(list): a list of activitiy(ies) dictionary(ies).
    activity(dict):The activity and its details.
        
    Returns:
    list: a list of activitiy(ies) dictionary(ies) with new activity added.

    Raises:
    ValueError: if list_activities is a integer.

    Example:
        >>>add_activity([], {"name" : "run","description" : "slow run","time" : 200 })
        [{"name" : "run","description" : "slow run","time" : 200 }]
    """
    
    list_activities.append(activity)
    print("Activity added!")
    return list_activities

def total_time_spent(list_activities): #STEVEN
    total = 0
    for i in list_activities:
        total += int(i["time"])
    return total

def delete_activity(list_activities): # Yiming
    """
    Description:
    Deletes a activity from the activity list.
    The function asks user the enter the activity they want to delete and delete if it exists.

    Parameters:
    list_activities(list): a list of activitiy(ies) dictionary(ies).

    Returns:
    list: a list of activitiy(ies) dictionary(ies) with a activity deleted.
    """
        
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

def update_activity(list_activities): # Yiming
    """
    Description:
    Changes the details of a activity.
    The functions ask users to which activity to change, if the activity exists, asks users to enter the new details.

    Parameters:
    list_activities(list): a list of activitiy(ies) dictionary(ies).

    Returns:
    list: a list of activitiy(ies) dictionary(ies) with the details of a activity changed.
    """
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

def change_time(list_activities):
    """
    Description:
    Changes the time spent of a activity.
    THe function asks the users to choose a activity they want to change time, if it exists, asks them to enter the new time.
    The function will check whether the list is empty first.

    Parameters:
    list_activities(list): a list of activitiy(ies) dictionary(ies).

    Returns:
    list: a list of activitiy(ies) dictionary(ies) with the details of a activity changed.
    
    """
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
    """
    Description:
    Saves the activity(ies) data to another file "Data.txt" so that it can be stored for further use.

    Parameters:
    list_activities(list): a list of activitiy(ies) dictionary(ies).

    Returns:
    str: messaged stored in Data.txt
    """
    with open("Data.txt", "w") as f:
        for a in list_activities:
            f.write(f"{a['name']},{a['time']},{a['description']}\n")

def read_data(): #Leon
    """
    Description:
    Reads activity(ies) data from the file "Data.txt" and converts it back into data type ready to be used.

    Parameters:
    None

    Returns:
    list_activities(list): a list of activitiy(ies) dictionary(ies).

    Raise:
    FileNotFoundError: if the file does not exists.
    """
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
  

#Main Program 
def main():
    #Need Comments
    list_activities = read_data()
    while True:
        print("="*118)
        print("\t\t\t\t\t\tWELCOME TO FITNESS TRACKER")
        print("="*118)
        print("1. Add Activity (With time) | 2. View List | 3. Remove Activitiy | 4. Update Activity | 5. Change time spent | 6. Quit")
        try:
            choice = int(input("Select option from 1-6: "))
        except: 
            print("Invalid input!")
            continue
        if choice == 1:
            n = input("Enter name of the activity: ")
            d = input("Add some note for your activity: ")
            t = int(input("Enter time you would spend on this activity in MINUTES: "))

            new_activity = create_activity(n, d, t)
            my_activity = add_activity(list_activities, new_activity)
            save_data(list_activities)
        elif choice == 2:
            display_list(list_activities)
            print(f"Total time spent: {total_time_spent(list_activities)} Minutes")
        elif choice == 3:
            delete_activity(list_activities)
            save_data(list_activities)
        elif choice == 4:
            update_activity(list_activities)
            save_data(list_activities)
        elif choice == 5:
            change_time(list_activities)
            save_data(list_activities)
        elif choice == 6:
            print("Saving data... Goodbye.")
            save_data(list_activities)
            break 
        else:
            print("Invalid input! Please select from 1-6.")
main()
