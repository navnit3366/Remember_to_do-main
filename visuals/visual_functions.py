import json

def set_time_spin():
    with open("data/times.json", "r") as file:
        times = json.load(file)
        items = []
        for item in times:
            items.append(item)
        file.close()
    with open("data/time.txt", "r") as file:
        time = file.read()
        file.close()
    return items, time

def get_tasks():
    try:
        task_list = []
        with open("data/rememberlist.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                if not tasks[task]:
                    task_list.append(task)
            file.close()
        return task_list
    except json.decoder.JSONDecodeError:
        return task_list

def get_all_tasks():
    try:
        task_list = []
        with open("data/rememberlist.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                task_list.append(task)
            file.close()
        return task_list
    except json.decoder.JSONDecodeError:
        return task_list

def update_tasks_made(tasks):
    try:
        with open("data/rememberlist.json", "r") as file:
            task_file = json.load(file)
            for task in tasks:
                task_file[task] = True
            file.close()
        with open("data/rememberlist.json", "w") as file:
            file.write(json.dumps(task_file))
            file.close()
    except json.decoder.JSONDecodeError:
        pass

def delete_tasks(tasks):
    with open("data/rememberlist.json", "r") as file:
        list = json.load(file)
        for i in tasks:
            del list[i]
        file.close()
    with open("data/rememberlist.json", "w") as file:
        json.dump(list, file)
        file.close()

def add_tasks(tasks):
    with open("data/rememberlist.json", "r") as file:
        list = json.load(file)
        for i in tasks:
            if i not in list:
                list.update({i: False})
        file.close()
    with open("data/rememberlist.json", "w") as file:
        json.dump(list, file)
        file.close()
        

def save_time(time):
    with open("data/time.txt", "w") as file:
            file.write(time)
            file.close()