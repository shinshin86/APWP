# -*- coding: utf8  -*-
import re
import configparser
import csv
import postdata
from datetime import datetime as dt
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo


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
    
    post_info = WordPressPost()
    # debug print
    print("debug print => config : " + url + " : " + user + " : " +  password)

    # Post lists
    post_list = []

    # Reading a "post"
    postsReader = csv.reader(open('post/postdata.csv', 'r'), delimiter=',')

    for i,row in enumerate(postsReader):
        if i != 0:
            post_list.append(row)
    for i,p in enumerate(post_list):
        print(i)
        send_to_wordpress(p,post_info,client)


def send_to_wordpress(post,post_info,client):

    for i,p in enumerate(post):
        print("debug print => " + p)
        
        # Set a title
        if i == 0:
            post_info.title = p

        # Set a content
        if i == 1:
             post_info.content = postdata.take_postdata(p)

        # Set a tag & category
        if i == 2:
            post_tag = "'post_tag': " + p + "]"

        if i == 3:
            post_category = "'category': [" + p + "]"
            post_info.terms_names = {}
            post_info.terms_names = post_tag
            post_info.terms_names = post_category

        # Set a date
        if i == 4:
            post_info.date = dt.strptime(p, '%Y-%m-%d')

        # Set a Image file(Thumbnail)
        if i == 5:

            # set to the path to your "Image file"
            filename = postdata.take_image(p)

            # prepare metadata
            data = {
                'name': 'picture.png',
                'type': 'image/jpeg',  # mimetype
            }

            # Read the binary file
            with open(filename, 'rb') as img:
                data['bits'] = xmlrpc_client.Binary(img.read())

            response = client.call(media.UploadFile(data))

            attachment_id = response['id']
            post_info.thumbnail = attachment_id

            # wordpress post
            client.call(NewPost(post_info))


if __name__ == '__main__':
    main()
