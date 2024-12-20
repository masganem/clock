from timesheet.read_timesheet import read_timesheet


def is_clocked_in(task):
    timesheet = read_timesheet(task)
    if len(timesheet) == 0 or len(timesheet[-1]) == 0:
        return False
    last_row = timesheet[-1]
    return last_row[1] == '-'