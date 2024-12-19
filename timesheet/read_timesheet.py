def read_timesheet(task):
    with open(f'{task}.csv', 'r') as f:
        rows = list(map(lambda x: x.split(','), f.readlines()))
        return rows