import urllib.request
import os
from os import path

raw_data_source = "https://raw.githubusercontent.com/tabatkins/wordle-list/main/words"
directory_name = "WordleData"
file_name = "wordList.txt"


def retrieve_data():
    url_request = urllib.request.urlopen(raw_data_source)
    data = url_request.read().decode("utf-8")
    return data


def store_data():
    if os.path.isfile(get_file_path()) == False:
        data = retrieve_data()
        os.mkdir(directory_name)
        file = open(get_file_path(), "w")
        file.write(data)
        file.close


def get_file_path():
    return path.join(directory_name, file_name)
