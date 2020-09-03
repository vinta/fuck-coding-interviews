# coding: utf-8
import unittest

from data_structures.trees.trie import Trie


class TrieNodeTest(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test__len__(self):
        self.assertEqual(len(self.trie), 0)

    def test_insert(self):
        with self.assertRaises(ValueError):
            self.trie.insert('')

    def test_search(self):
        self.assertEqual(self.trie.search(''), False)

    def test_startsWith(self):
        self.assertEqual(self.trie.startsWith(''), True)

    def test_integration(self):
        self.trie.insert('apple')
        self.assertEqual(len(self.trie), 1)
        self.assertEqual(self.trie.search('apple'), True)
        self.assertEqual(self.trie.search('app'), False)
        self.assertEqual(self.trie.startsWith('app'), True)

        self.trie.insert('app')
        self.assertEqual(len(self.trie), 2)
        self.assertEqual(self.trie.search('app'), True)
        self.assertEqual(self.trie.startsWith('app'), True)

        self.trie.insert('hammer')
        self.assertEqual(len(self.trie), 3)
        self.assertEqual(self.trie.search('hammers'), False)
        self.assertEqual(self.trie.startsWith('hammers'), False)


if __name__ == '__main__':
    unittest.main()
