import unittest
import functions as fn

class TestSiteGenerate(unittest.TestCase):
    def test_extract_title(self):
        title = fn.extract_title("# Mi title")
        self.assertEqual(title, "Mi title")
    
    def test_title_extract_fail(self):
        with self.assertRaises(Exception):
            title = fn.extract_title("Mi title is wrong")
    
    
if __name__ == "__main__":
    unittest.main()
