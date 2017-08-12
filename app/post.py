# -*- coding: utf8  -*-
import re
import configparser
import csv
import os
from os import path
from config_util import config_read

def fetch_content(arg_file):
    conf = config_read()
    contents_path = conf["contents"]

    files = os.listdir(contents_path)

    for file in files:
        if file == arg_file:
            title = file
            post_text = []
            post_title = title.rstrip('\.txt')
            with open(contents_path + "/" + file, encoding='utf-8') as f:
                for line in f:
                    post_text.append(line)

    return "".join(post_text)

def fetch_image(arg_file):
    conf = config_read()
    postdatas_path = conf["images"]

    files = os.listdir(postdatas_path)
    for f in files:
        if f == arg_file:
            return path.join(postdatas_path, f)
