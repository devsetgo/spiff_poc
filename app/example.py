# -*- coding: utf-8 -*-
""" An example of functions in the common library"""
import time
from datetime import date
from datetime import datetime
from pathlib import Path

import requests

# remove loguru and place your favorite logging mechanism
from loguru import logger

from com_lib.file_functions import create_sample_files
from com_lib.file_functions import delete_file
from com_lib.file_functions import get_data_directory_list
from com_lib.file_functions import open_json
from com_lib.file_functions import open_text
from com_lib.file_functions import save_text
from com_lib.folder_functions import get_directory_list
from com_lib.folder_functions import last_data_files_changed
from com_lib.folder_functions import make_folder
from com_lib.folder_functions import remove_folder
from com_lib.logging_config import config_logging

config_logging()


def call_folder_functions():

    print("make dir")
    make_dir()

    print("last change")
    last_change()

    print("delete folder")
    delete_dir()


def dir_list_func():
    dir_list = get_directory_list("data")
    # print(dir_list)
    for i in dir_list:
        x = str(i)
        if "csv" in x:
            p = i
            name = "data/cs_v"
            x = p.rename(name)

    # Pause so you can see the change
    time.sleep(5)

    dir_list = get_directory_list("data")
    # print(dir_list)
    for i in dir_list:
        x = str(i)
        if "cs_v" in x:
            p = i
            name = "data/csv"
            x = p.rename(name)


def last_change():
    directory_to__files: str = "data"
    file_directory = f"{directory_to__files}"
    directory_path = Path.cwd().joinpath(file_directory)
    str(directory_path)
    time_stamp, file_path = last_data_files_changed(directory_path)
    print(time_stamp, file_path)

    if "2019" in str(file_path):
        print("yes its there")


def make_dir():
    print("wait make")
    time.sleep(2)
    for _ in range(2):

        d = datetime.now().strftime("%Y-%M-%H-%M-%S-%f")
        # print(d)
        directory_to__files: str = "data"
        file_directory = f"{directory_to__files}/x-{d}"
        directory_path = Path.cwd().joinpath(file_directory)
        make_folder(directory_path)
        print(directory_path.is_dir())


def delete_dir():
    print("wait delete")
    time.sleep(10)
    date_object = date.today()
    # get year from date object
    year = date_object.strftime("%Y")

    file_list = get_directory_list("data")
    # print(file_list)
    for i in file_list:
        # time.sleep(1)
        f = str(i)
        if year in f:
            # delete directory
            remove_folder(i)


def get_data():
    filename: str = "test_1.json"
    try:
        result: dict = open_json(filename)
        print(result)
    except Exception as e:
        # print(e)
        logger.error(e)


def make_sample():
    filename: str = "sample"
    sample_size: int = 2
    try:
        create_sample_files(filename, sample_size)
    except Exception as e:
        # print(e)
        logger.error(e)


def dir_list():
    directory: str = "json"
    try:
        directory_list: list = get_data_directory_list(directory)
    except Exception as e:
        print(e)

    try:
        for i in directory_list:
            result: dict = open_json(i)
            count = 0
            for n in result:
                x = n["name"]
                print(x)
                count += 1
            print(count)
    except Exception as e:
        logger.error(e)


def text_process():
    url = "https://devsetgo.com"
    r = requests.get(url)
    logger.info(f"fetching from {url}")
    data = r.text
    file_name = f"test_1.html"
    save_text(file_name, data)
    logger.info(f"save file {file_name}")

    # read file
    logger.info(f"fetching from file {file_name}")
    read_data = open_text(file_name)
    print(read_data)
    logger.info(f"read of file {file_name} complete")
    # uncomment line below if you want to see the contents of the file.
    # print(read_data)


def go_delete():
    file_name = [
        "sample.csv",
        "sample.json",
        "test_1.html",
        "/test.csv",
        r"\error.json",
    ]

    for f in file_name:
        result = delete_file(f)
        print(result)


if __name__ == "__main__":
    # print("get data")
    # get_data()
    # print("make sample")
    # make_sample()
    # print("dir list")
    # dir_list()
    # print("folder functions")
    # call_folder_functions()
    # print("delete folder")
    # delete_dir()
    # text_process()
    # go_delete()
    make_dir()
