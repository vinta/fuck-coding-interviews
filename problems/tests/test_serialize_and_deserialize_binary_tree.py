# coding: utf-8
import unittest

from problems.serialize_and_deserialize_binary_tree import Codec
from problems.utils.leetcode import deserialize_tree_str
from problems.utils.leetcode import serialize_treenode


class TestCase(unittest.TestCase):
    def test(self):
        test_data = [
            {'input': '[]'},
            {'input': '[-1,0,1]'},
            {'input': '[1,2,3,null,null,4,5]'},
        ]
        for data in test_data:
            tree_str = data['input']
            with self.subTest(tree_str=tree_str):
                root = deserialize_tree_str(tree_str)
                codec = Codec()
                expected_root = codec.deserialize(codec.serialize(root))
                self.assertEqual(tree_str, serialize_treenode(expected_root))


if __name__ == '__main__':
    unittest.main()
