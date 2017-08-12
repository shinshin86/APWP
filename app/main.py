# -*- coding: utf8  -*-
import re
import configparser
import csv
from config_util import config_read
from os import path
from postdata_csv import read_to_csv
from postdata_json import read_to_json
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo


def main():
    client = get_connect_client()

    post = WordPressPost()

    postfile_path = get_post_dir()

    # csv
    #datas = read_to_csv(path.join(postfile_path, 'postdata.csv'), client)

    # json
    datas = read_to_json(path.join(postfile_path, 'postdata.json'), client)

    for i in datas:
        send_to_wordpress(i, post, client)


def get_post_dir():
    conf = config_read()
    return conf["postdir"]


def get_connect_client():
    conf = config_read()

    url = conf["connect_wp"]
    user = conf["connect_user"]
    password = conf["connect_pass"]

    # debug print
    # print("debug print => config : " + url + " : " + user + " : " +  password)

    return Client(url,user,password)


def send_to_wordpress(data,post,client):
    post.title = data['title']
    post.content = data['content']
    post.terms_names = data['terms_names']
    post.date = data['date']
    post.thumbnail = data['thumbnail']
    post.post_status = data['post_status']

    client.call(NewPost(post))

if __name__ == '__main__':
    main()
