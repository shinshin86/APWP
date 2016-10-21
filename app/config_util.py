import configparser


def read():
    conf_connect = configparser.ConfigParser()
    conf_post = configparser.ConfigParser()
    conf_connect.read('./config/connect_wp.cfg')
    conf_post.read('./config/postdata_dir.cfg')
    conf_dict = {}
    conf_dict = {"connect_wp" : str(conf_connect.get('connect_info','url')),
                 "connect_user" : str(conf_connect.get('connect_info','user')),
                 "connect_pass" : str(conf_connect.get('connect_info','password')),
                 "postdatas_path" : str(conf_post.get('postdata','content')),
                 "postimages_path" : str(conf_post.get('postdata', 'image'))}
    return conf_dict


