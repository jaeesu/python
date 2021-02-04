import datetime

def convert_datetime(unixtime):
    #date = datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')
    date = datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d')
    return date # format : str


