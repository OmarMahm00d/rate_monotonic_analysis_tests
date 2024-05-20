import math
print("Hello, We gonna discuss the schedulability of tasks if we're using RMA approach using punch of tests.")


def bound_test(tasks):
    n = len(tasks)
    utilization_sum = sum(task['completion_time'] / task['period'] for task in tasks)
    bound = n * (2 ** (1 / n) - 1)
    return utilization_sum <= bound

def completion_test(tasks):
    for task in tasks:
        task['remaining_time'] = task['completion_time']

    time = 0
    while any(task['remaining_time'] > 0 for task in tasks):
        for task in sorted(tasks, key=lambda t: t['period']):
            if time % task['period'] == 0:
                task['remaining_time'] = task['completion_time']
            if task['remaining_time'] > 0:
                task['remaining_time'] -= 1
                break
        time += 1

    return all(task['remaining_time'] <= 0 for task in tasks)

def main():
    tasks = []

    n = int(input("Enter number of tasks: "))
    for i in range(n):
        period = float(input(f"Enter period for task {i + 1}: "))
        completion_time = float(input(f"Enter completion time for task {i + 1}: "))
        tasks.append({'period': period, 'completion_time': completion_time})

    if bound_test(tasks):
        print("Bound Test: PASS")
    else:
        print("Bound Test: FAIL")

    if completion_test(tasks):
        print("Completion Test: PASS")
    else:
        print("Completion Test: FAIL")

if __name__ == "__main__":
    main()
