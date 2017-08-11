import unittest
import os
import shutil
import configparser
from app.post import fetch_content
from app.post import fetch_image
class PostTest(unittest.TestCase):
    def setUp(self):
        if os.path.isdir("./tests/files"):
            shutil.copytree("./tests/files/post", "./post")

        self.conf = configparser.ConfigParser()
        self.conf.read('./config/postdata_dir.cfg')

    def tearDown(self):
        shutil.rmtree("./post")

    def test_fetch_content(self):
        test_content = "test.txt"
        self.assertTrue(fetch_content(test_content))


    def test_fetch_image(self):
        test_image = "sample_image.png"
        self.assertTrue(fetch_image(test_image))

if __name__ == "__main__":
    unittest.main()
