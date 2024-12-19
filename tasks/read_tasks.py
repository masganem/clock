def read_tasks():
    with open('tasks.csv', 'r') as f:
        return set(f.read().split(','))