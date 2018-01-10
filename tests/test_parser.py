from .context import malc0de
import unittest


class ConnectTestSuite(unittest.TestCase):

    def test_malcode_feed_item(self):
        ip = malc0de.Malcode.get_rss_items()[:1]
        self.assertEqual(ip[0].__class__.__name__, 'Malcode', 'Datatype mis-matched.')

    def test_malcode_feed_count(self):
        ip = malc0de.Malcode.get_rss_items()
        self.assertEqual(len(ip), 500, 'Found a total of {0} items in feed.'.format(len(ip)))


if __name__ == '__main__':
    unittest.main()
