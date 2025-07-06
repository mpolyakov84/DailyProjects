import unittest
from images_downloader import get_img_links

class TestsImagesDownloader(unittest.TestCase):

    def test_get_img_links(self):
        links = get_img_links()
        self.assertIsNotNone(links)