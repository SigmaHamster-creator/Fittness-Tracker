def delete_activity(list_activities, name):
        for a in list_activities:
            if a["name"] == name:
                list_activities.remove(a)
            else:
                print(f"can not found activity {name}")