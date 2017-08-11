# -*- coding: utf8  -*-

def read_to_csv(filepath):
    postsReader = csv.reader(open('post/postdata.csv', 'r'), delimiter=',')
    return postsReader
