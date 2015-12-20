# -*- coding: utf8  -*-
import re
import configparser
import csv

# Remove a comment later!
# from wordpress_xmlrpc import Client, WordPressPost



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
postdata = []
index = []
title = []
content = []
tags = []
category = []
date = []


# Reading a "PostData"
postsReader = csv.reader(open('post/postdata.csv', 'r'), delimiter=',')
for i,row in enumerate(postsReader):
    if i != 0:
        for j,column in enumerate(row):
            if j == 0:
                index.append(i)
                title.append(column)
            if j == 1:
                content.append(column)
            if j == 2:
                tags.append(column)
            if j == 3:
                category.append(column)
            if j == 4:
                date.append(column)
postdata.append(index)
postdata.append(title)
postdata.append(content)
postdata.append(tags)
postdata.append(category)
postdata.append(date)



# debug
for i,row in enumerate(postdata):
    print(row)