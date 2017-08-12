# -*- coding: utf8  -*-
import csv
from datetime import datetime as dt
from post import fetch_content, fetch_image
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

def read_to_csv(filepath, client):
    post_list = []

    postsReader = csv.reader(open('post/postdata.csv', 'r'), delimiter=',')

    for i,row in enumerate(postsReader):
        if i != 0:
            pdict = {}
            for j,p in enumerate(row):
                if j == 0:
                    pdict['id'] = p

                if j == 1:
                    pdict['title'] = p

                if j == 2:
                    pdict['content'] = fetch_content(p)

                if j == 3:
                    post_tag = p

                if j == 4:
                    category = p
                    pdict['terms_names'] = { 'post_tag':[post_tag],'category':[category]}

                if j == 5:
                    pdict['date'] = dt.strptime(p, '%Y-%m-%d  %H:%M:%S')

                if j == 6:
                    filename = fetch_image(p)

                    # prepare metadata
                    data = {
                        'name': p,
                        'type': 'image/png',
                    }

                    # Read the binary file
                    with open(filename, 'rb') as img:
                        data['bits'] = xmlrpc_client.Binary(img.read())

                    response = client.call(media.UploadFile(data))

                    attachment_id = response['id']
                    pdict['thumbnail'] = attachment_id

                    # TODO
                    # pdict['post_status'] = 'publish'
                    # development env
                    pdict['post_status'] = 'draft'

                    post_list.append(pdict)

    return post_list


