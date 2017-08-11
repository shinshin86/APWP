# -*- coding: utf8  -*-
import os.path
import re
import configparser
import csv
import post
import config_util
from postdata_csv import read_to_csv
from datetime import datetime as dt
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo


def main():
    # Read a "Connect Info"
    conf = config_util.read()

    # Connect Info
    url = conf["connect_wp"]
    user = conf["connect_user"]
    password = conf["connect_pass"]

    post = WordPressPost()
    # debug print
    print("debug print => config : " + url + " : " + user + " : " +  password)

    client = Client(url,user,password)

    # Post lists
    post_list = []

    # Reading a "post"
    postfile_path = 'post'

    postsReader = read_to_csv(os.path(postfile_path, 'postdata.csv'))
    # postsReader = csv.reader(open('post/postdata.csv', 'r'), delimiter=',')
    # postsReader = csv.reader(open('post/postdata.json', 'r'), delimiter=',')

    for i,row in enumerate(postsReader):
        if i != 0:
            post_list.append(row)

    for i,p in enumerate(post_list):
        send_to_wordpress(p,post,client)

# Post process "Wordpress"
def send_to_wordpress(postdata,post,client):

    for i,p in enumerate(postdata):
        # Set a title
        if i == 1:
            post.title = p

        # Set a content
        if i == 2:
             post.content = postdata.fetch_content(p)

        # Set a tag & category
        if i == 3:
            post_tag = p

        if i == 4:
            post_category = p
            post.terms_names = { 'post_tag':[post_tag],'category':[post_category]}

        # Set a date
        if i == 5:
            post.date = dt.strptime(p, '%Y-%m-%d  %H:%M:%S')

        # Set a Image file(Thumbnail)
        if i == 6:

            # set to the path to your "Image file"
            filename = postdata.fetch_image(p)

            # prepare metadata
            data = {
                'name': p,
                'type': 'image/png',  # mimetype
            }

            # Read the binary file
            with open(filename, 'rb') as img:
                data['bits'] = xmlrpc_client.Binary(img.read())

            response = client.call(media.UploadFile(data))

            attachment_id = response['id']
            post.thumbnail = attachment_id

            client.call(NewPost(post))

if __name__ == '__main__':
    main()
