#Test 3 functions
#add_activity(str/str)

#remove_activity(str)

#Update_activity(str/str)
class Menu:

    def __init__(self, time, description):
        self.time = time
        self.description = description
    def __str__(self):
        return f"time: {self.time}, description: {self.description}"
#add_activity(str/str)
def add_activity(name, time, description):
    activities[name] = Menu(time, description)
#remove_activity(str)
def remove_activity(name):
    del activities[name]
#Update_activity(str/str)
def update_acttivity(name,time, description):
    activities[name].time = time
    activities[name].description = description

activities = {}

#function tests
#try add
add_activity(input("name: "), input("time: "), input("description: "))
#search 
search = input("Which activity do you want to search")
print("name: "+ search + ", " , activities[search])
#try update
update_acttivity(input("name: "), input("time: "), input("description: "))
#search again
search = input("Which activity do you want to search")
print("name: "+ search + ", " , activities[search])
#try remove
remove_activity(input("name: "))
#print activities
print(activities)
#try search
try:
    search = input("Which activity do you want to search")
    print("name: "+ search + ", " , activities[search])
except KeyError:
    print("This activity was deleted!")
# I will test another method, dictionary[dictionary] method next time
# Yiming
