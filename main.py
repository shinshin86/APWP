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
    index = []
    title = []
    content = []
    tags = []
    category = []
    date = []
    image = []


    # Reading a "post"
    postsReader = csv.reader(open('post/postdata.csv', 'r'), delimiter=',')
    for i,row in enumerate(postsReader):
        if i != 0:
            for j,column in enumerate(row):
                if j == 0:
                    index.append(i)
                    title.append(column)
                if j == 1:
                    # What a wrong here?
                    # list => str
                    content.append("".join(postdata.take_postdata(column)))
                if j == 2:
                    tags.append(column)
                if j == 3:
                    category.append(column)
                if j == 4:
                    date.append(column)
                if j == 5:
                    image.append(postdata.take_image(column))
    post.append(index)
    post.append(title)
    post.append(content)
    post.append(tags)
    post.append(category)
    post.append(date)
    post.append(image)



    # debug
    for i,row in enumerate(post):
        print(row)



if __name__ == '__main__':
    main()
