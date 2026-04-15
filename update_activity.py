def update_activity(list_activities,name,time, discription):
    for a in list_activities:
        if a["name"] == name:
            a["time"] = time
            a["discription"] = discription