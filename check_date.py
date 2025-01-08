import re

def check_date(date):
    date_pattern = r'^((0[1-9]|1[0-2])/(0[1-9]|1[0-9]|2[0-8]))$|^((0[13578]|1[02])/(29|30|31))$|^((0[469]|11)/(29|30))$'
    if re.search(date_pattern, date):
        return True
    else:
        return False

