import configparser


def read():
    conf = configparser.SafeConfigParser()
    conf_connect.read('./config/connect_wp.cfg')
    conf_post.read('./config/postdata_dir.cfg')
    conf_dict = {}
    conf_dict = {"connect_wp" : str(conf_connect.get('connect_info','url')),
                 "connect_user" : str(conf_connect.get('connect_info','user')),
                 "connect_pass" : str(conf_connect.get('connect_info','password')),
                 "postdatas_path" : str(conf_post.get('postdata','content'))}
    return conf_dict


