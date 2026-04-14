
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
def save_data(activities):
    with open ("Data.txt","w") as f:
            for n,m in activities.items():
                f.write(n + "," + str(m.time) + "," + str(m.description) + "\n")

#This converts the activities back into dict
def read_data():
    activities = {}
    try:
        with open ("Data.txt","r") as f:
            for line in f:
                n,time,description = line.strip().split(",")
                activities[n] = Menu(time, description)
        return activities
    except FileNotFoundError:
        print("The file does not exist.")
    return activities


activities = {}

activities = read_data()
add_activity(input("name: "), input("time: "), input("description: "))
save_data(activities)
new_activities = read_data()
for name,data in new_activities.items():
    print(name,data)


