from timesheet.read_timesheet import read_timesheet


def is_clocked_in(task):
    timesheet = read_timesheet(task)
    last_row = timesheet[-1]
    return last_row[1] == '-'