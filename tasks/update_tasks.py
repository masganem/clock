def update_tasks(tasks):
    with open('tasks.csv', 'w') as f:
        return f.write(','.join(tasks))