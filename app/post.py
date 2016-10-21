# -*- coding: utf8  -*-
import re
import configparser
import csv
import os
import app.config_util
def take_postdata(arg_file):
    # Read a "Connect Info"
    conf = app.config_util.read()
    postdatas_path = conf["postdatas_path"]

    files = os.listdir(postdatas_path)
    for file in files:
        if file == arg_file:
            title = file
            post_text = []
            post_title = title.rstrip('\.txt')
            with open(postdatas_path + "/" + file, encoding='utf-8') as f:
                for line in f:
                    post_text.append(line)

    return "".join(post_text)

def take_image(arg_file):
    # Read a "Connect Info"
    conf = app.config_util.read()
    postdatas_path = conf["postimages_path"]

    files = os.listdir(postdatas_path)
    for file in files:
        if file == arg_file:
            return postdatas_path + '/' + file
