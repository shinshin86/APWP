import configparser


def config_read():
    conf_connect = configparser.ConfigParser()
    conf_post = configparser.ConfigParser()
    conf_connect.read('./config/connect_wp.cfg')
    conf_post.read('./config/postdata_dir.cfg')
    conf_dict = {}
    conf_dict = {"connect_wp" : str(conf_connect.get('connect_info','url')),
                 "connect_user" : str(conf_connect.get('connect_info','user')),
                 "connect_pass" : str(conf_connect.get('connect_info','password')),
                 "postdir" : str(conf_post.get('postdata', 'postdata')),
                 "contents" : str(conf_post.get('postdata','content')),
                 "images" : str(conf_post.get('postdata', 'image')),
                 "filetype" : str(conf_post.get('postdata', 'filetype'))}
    return conf_dict


