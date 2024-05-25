#Write log to file
#param: message
import os
import pathlib
import datetime

def gen_log_text(message):
    timestamp = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    return timestamp + ' - ' + message

def write_logging(message, file_name='log.txt'):
    files_directory = os.path.join(str(pathlib.Path(__file__).parent.resolve()),'log',file_name)
    with open(files_directory, 'a') as file:
        file.write(message + '\n')
        
def write_complete_logging(message):
    write_logging(gen_log_text(message), 'complete_log.txt')
    
def write_complete_list_logging(message=[]):
    for msg in message:
        write_logging(msg, 'complete_log.txt')
    
def write_error_logging(message):
    write_logging(gen_log_text(message), 'error_log.txt')


