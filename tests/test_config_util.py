import unittest
from app.config_util import read
class ConfigUtilTest(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_read(self):
        conf = read()
        self.assertTrue(conf["connect_wp"])
        self.assertTrue(conf["connect_user"])
        self.assertTrue(conf["connect_pass"])
        self.assertTrue(conf["postdatas_path"])


if __name__ == "__main__":
    unittest.main()



