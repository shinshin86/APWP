import unittest
import os
import shutil
import configparser
from app.post import take_postdata
from app.post import take_image
class PostTest(unittest.TestCase):
    def setUp(self):
        if os.path.isdir("./tests/files"):
            shutil.copytree("./tests/files/post", "./app/post")

        self.conf = configparser.ConfigParser()
        self.conf.read('./config/postdata_dir.cfg')

    def tearDown(self):
        shutil.rmtree("./app/post")

    def test_take_postdata(self):
        test_content = "test.txt"
        self.assertTrue(take_postdata(test_content))


    def test_take_image(self):
        test_image = "sample_image.png"
        self.assertTrue(take_image(test_image))

if __name__ == "__main__":
    unittest.main()
