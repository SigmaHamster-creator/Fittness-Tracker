# Allow the user to record a fitness activity with name/description.
# Enter the time spent on the fitness activity (eg. in minutes).
# Allow the user to view a list of all recorded activities.
# Clearly show the time spent for each of the recorded activities.
# Allow the user to change/update the time spent on each activity.
# Save fitness data so it is available when the program is run again.

class Menu:

    def __init__(self, name, description):
        self._name = name
        self._description = description 

    def show_menu(self):
        self.edit()
        print(f"\t\t{self._name}")
        self.edit()
        for i in range(len(self._description)):
            print(f"{i+1}. {self._description[i]}")

    def edit(self):
        print("="*50)
    
    def take_user_input(self):
        activity = int(input("Enter the number of activity in the menu:"))
        self.edit()
        while activity < 0 or activity > len(self._description):
            print("Invalid input, please try again")
            self.show_menu()
            activity = int(input("Enter the number of activity in the menu:"))
        return activity

m1 = Menu("Main Menu",["add","remove","update"])
m1.show_menu()
print(m1.take_user_input())