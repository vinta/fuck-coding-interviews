# coding: utf-8
import unittest

from data_structures.trees.binary_tree_serialization import LevelorderCodec


class LevelorderCodecTest(unittest.TestCase):
    def setUp(self):
        self.codec = LevelorderCodec()

    def test(self):
        test_data = [
            {'input': '[]'},
            {'input': '[1,2,3,4,null,2,4,null,null,4]'},
            {'input': '[1,2,3,null,4]'},
            {'input': '[1,2,3,null,null,4,5]'},
            {'input': '[1,null,2,3]'},
            {'input': '[1,null,2,null,3]'},
            {'input': '[2,1,3]'},
            {'input': '[3,1,null,null,2]'},
            {'input': '[3,2,null,1]'},
            {'input': '[3,9,20,null,null,15,7]'},
            {'input': '[4,2,7,1,3,6,9]'},
            {'input': '[5,4,7,3,null,2,null,-1,null,9]'},
            {'input': '[8,3,10,1,6,null,14,null,null,4,7,13]'},
        ]
        for data in test_data:
            tree_str = data['input']
            with self.subTest(tree_str=tree_str):
                root = self.codec.deserialize(tree_str)
                expected = self.codec.serialize(root)
                self.assertEqual(tree_str, expected)


if __name__ == '__main__':
    unittest.main()
