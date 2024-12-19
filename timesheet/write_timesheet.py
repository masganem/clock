def write_timesheet(task, timesheet):
    with open(f'{task}.csv', 'w') as f:
        rows = list(map(lambda x: (','.join(x)).strip() + '\n', timesheet))
        f.writelines(rows)