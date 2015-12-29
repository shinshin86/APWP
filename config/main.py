# -*- coding: utf8  -*-
import re
import configparser
import csv
import postdata
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

def main():
    # Read a "Connect Info"
    conf = configparser.SafeConfigParser()
    conf.read('config/connect_wp.cfg')
    connect_wp = str(conf.get('connect_info','url'))
    connect_user = str(conf.get('connect_info','user'))
    connect_pass = str(conf.get('connect_info','password'))


    # Connect Info
    url = connect_wp
    user = connect_user
    password = connect_pass

    # debug
    print("debug print => config : " + url + " : " + user + " : " +  password)


    # lists
    post = []

    # Reading a "post"
    postsReader = csv.reader(open('post/postdata.csv', 'r'), delimiter=',')
    # ２次元配列で各項目をそれぞれ項目して、一列ずつポスト処理を行えるようにしたい
    for i,row in enumerate(postsReader):
        if i != 0:
            post.append(row)
    for i,p in enumerate(post):
        print(i)
        send_to_wordpress(p)


def send_to_wordpress(post):
    for p in post:
        print("debug : " + p)


if __name__ == '__main__':
    main()
