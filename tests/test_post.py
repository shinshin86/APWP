import unittest
import os
import shutil
import configparser
class PostTest(unittest.TestCase):
    def setUp(self):
        if os.path.isdir("./tests/files"):
            shutil.copytree("./tests/files/post", "./app/post")

        self.conf = configparser.ConfigParser()
        self.conf.read('./config/postdata_dir.cfg')

    def tearDown(self):
        shutil.rmtree("./app/post")

    def test_take_postdata(self):
        postdatas_path = str(self.conf.get('postdata','content'))
        files = os.listdir(os.path.join("app",postdatas_path))
        self.assertEqual(len(files), 2)


    def test_take_image(self):
        postdatas_path = str(self.conf.get("postdata", "image"))
        files = os.listdir(os.path.join("app", postdatas_path))
        self.assertEqual(len(files), 1)

if __name__ == "__main__":
    unittest.main()
