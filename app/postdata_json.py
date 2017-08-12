# -*- coding: utf8  -*-
import json
from datetime import datetime as dt
from post import fetch_content, fetch_image
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

def read_to_json(filepath, client):
    post_list = []
    with open(filepath, 'r') as f:
        json_data = json.load(f)
        for i in json_data:
            pdict = {}
            pdict['id'] = i['id']
            pdict['title'] = i['title']
            pdict['content'] = fetch_content(i['content_file'])
            post_tag = i['tag']
            category = i['category']
            pdict['terms_names'] = { 'post_tag':[post_tag],'category':[category]}
            pdict['date'] = dt.strptime(i['date'], '%Y-%m-%d  %H:%M:%S')

            filename = fetch_image(i['image'])
            data = {
                'name': i['image'],
                'type': 'image/png',
            }

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
