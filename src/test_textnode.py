import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a test node", "bold", "test.url")
        node2 = TextNode("This is a text node", "bold", "test.url")
        self.assertNotEqual(node, node2)
    
    def test_eq3(self):
        node = TextNode("This is a test node", "italic", "test.url")
        node2 = TextNode("This is a test node", "bold", "test.url")
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a test node", "bold", None)
        node2 = TextNode("This is a test node", "bold")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
