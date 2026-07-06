def productivity_report(activities):
    count = {}

    for activity in activities:
        name, task = activity.split()
        name = name.lower()

        if name in count:
            count[name] += 1
        else:
            count[name] = 1

    employees = list(count.items())

    def sort_by_name(item):
        return item[0]

    employees.sort(key=sort_by_name)

    # sort by task count
    def sort_by_count(item):
        return item[1]

    employees.sort(key=sort_by_count, reverse=True)

    for name, tasks in employees:
        print(name, tasks)


# input section
n = int(input())

# list to store activities
activities = []

for i in range(n):
    activity = input()
    activities.append(activity)

productivity_report(activities)
