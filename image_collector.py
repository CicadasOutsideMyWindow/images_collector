import os
import logging

#TODO: logging
#TODO: list subfolders

source_folder = ""
target_folder = ""
logname = ""
allowed_ext = ['.jpeg', '.jpg', '.png', '.mov', '.mp4', '.mp3', '.wav', '.ogg', '.3gp', '.pdf', '.wmv', '.mkv', '.mxf']

# ===== Logging configuration =====

logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)


def is_mediafile(filepath):
    filename, file_extension = os.path.splitext(filepath)
    return file_extension.lower() in allowed_ext


def move_file(filepath):
    filename, file_extension = os.path.splitext(filepath)
    os.rename((source_folder + '/%s' % os.path.basename(filepath)), (str(target_folder) + '/%s/%s' % (file_extension[1:], os.path.basename(filepath))))
    logging.info('File %s moved to %s' % (filename, str(target_folder) + '/%s/%s' % (file_extension[1:])))


def create_targets():
    for extension in allowed_ext:
        new_folder_path = target_folder + '/%s' % extension[1:]
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)
            logging.info('Folder created: %s' % new_folder_path)

def app():
    create_targets()
    files = os.listdir(source_folder)
    count = 0
    for file in files:
        if is_mediafile(file):
            move_file(file)
            count = count + 1
            print str(count) + ' files moved'


app()