from datetime import datetime
from timesheet.write_timesheet import write_timesheet
from timesheet.read_timesheet import read_timesheet


def clock_in(task, description = ''):
    timesheet = read_timesheet(task)
    new_row = [str(datetime.now()), '-', description]
    timesheet.append(new_row)
    write_timesheet(task, timesheet)