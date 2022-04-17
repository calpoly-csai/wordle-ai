import urllib.request
import os

raw_data_source = "https://gist.github.com/cfreshman/cdcdf777450c5b5301e439061d29694c"
directory_name = "WordleData"
file_name = "wordList.txt"


def retrieve_data():
    url_request = urllib.request.urlopen(raw_data_source)
    data = url_request.read().decode("utf-8")
    return data


def store_data():
    if os.path.isfile("./" + directory_name + "/" + file_name) == False:
        data = retrieve_data()
        os.mkdir(directory_name)
        file = open(directory_name + "/" + file_name, "w")
        file.write(data)
        file.close
