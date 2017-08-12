import unittest
from app.config_util import config_read
class ConfigUtilTest(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_config_read(self):
        conf = config_read()
        self.assertTrue(conf["connect_wp"])
        self.assertTrue(conf["connect_user"])
        self.assertTrue(conf["connect_pass"])
        self.assertTrue(conf["postdir"])
        self.assertTrue(conf["contents"])
        self.assertTrue(conf["images"])


if __name__ == "__main__":
    unittest.main()



