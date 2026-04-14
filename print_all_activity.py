def print_activities(act_lst: list):
    for i in act_lst():
        count = 1
        print(f"{count}. {i.get("name")} {i.get("description")} {i.get("time")}\n")
        count += 1