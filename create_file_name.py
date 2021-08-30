import datetime
def create_file_name():
    file_name = 'output' + '_' + str(datetime.datetime.now().hour) + '_' + str(datetime.datetime.now().minute) + '_' + str(datetime.datetime.now().second) + '.pdf'
    return file_name
