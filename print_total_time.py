def print_total_time(act_list: list):
    for i in act_list():
        total = 0
        total += i.get("time")
    
    print("Your total time spent on activities are ",total," minutes\n")