from datetime import datetime
from timesheet.write_timesheet import write_timesheet
from timesheet.read_timesheet import read_timesheet


def clock_out(task, description = ''):
    timesheet = read_timesheet(task)
    last_row = timesheet[-1]
    last_row[1] = str(datetime.now())
    if description != '':
        last_row[2] = description
    write_timesheet(task, timesheet)
    return get_time_diff(last_row[0], last_row[1])

    

def get_time_diff(time_str1, time_str2):
    start_time = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")
    end_time = datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S.%f")

    time_diff = end_time - start_time
    total_seconds = int(time_diff.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Format the result as "hh mm ss"
    formatted_time_diff = f"{hours:02}h {minutes:02}m {seconds:02}s"

    return formatted_time_diff