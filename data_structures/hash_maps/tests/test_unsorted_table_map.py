# coding: utf-8
import random
import unittest

from data_structures.hash_maps.unsorted_table_map import UnsortedTableMap


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_map = UnsortedTableMap()

        self.d1 = {'key': 'The phrase on the cover', 'value': "DON'T PANIC"}
        self.d2 = {'key': 'The answer to the ultimate question', 'value': 42}
        self.d3 = {'key': "God's final message", 'value': 'WE APOLOGIZE FOR THE INCONVENIENCE'}
        data = [self.d1, self.d2]

        self.map = UnsortedTableMap()
        self.dict = {}
        for d in data:
            self.map[d['key']] = d['value']
            self.dict[d['key']] = d['value']

    def test__len__(self):
        self.assertEqual(len(self.empty_map), 0)
        self.assertEqual(len(self.map), len(self.dict))

    def test__iter__(self):
        self.assertEqual(list(self.empty_map), [])
        self.assertCountEqual(list(self.map), list(self.dict))

    def test__setitem__(self):
        self.map[self.d2['key']] = -42
        self.dict[self.d2['key']] = -42
        self.map[self.d3['key']] = self.d3['value']
        self.dict[self.d3['key']] = self.d3['value']
        self.assertEqual(len(self.map), len(self.dict))
        self.assertCountEqual([(k, v) for k, v in self.map.items()], [(k, v) for k, v in self.dict.items()])

    def test__getitem__(self):
        with self.assertRaises(KeyError):
            self.map['NOT EXIST']

        self.assertEqual(self.map[self.d1['key']], self.dict[self.d1['key']])
        self.assertEqual(self.map[self.d2['key']], self.dict[self.d2['key']])

    def test__delitem__(self):
        with self.assertRaises(KeyError):
            del self.map['NOT EXIST']

        del self.map[self.d1['key']]
        del self.dict[self.d1['key']]
        self.assertEqual(len(self.map), len(self.dict))
        self.assertCountEqual([(k, v) for k, v in self.map.items()], [(k, v) for k, v in self.dict.items()])

    def test_integration(self):
        for i in range(1, random.randint(2, 1000)):
            self.map[i] = i
            self.dict[i] = i
            if i % 5 == 0:
                del self.map[i]
                del self.dict[i]

        self.assertEqual(len(self.map), len(self.dict))
        self.assertCountEqual(list(self.map.items()), list(self.dict.items()))


if __name__ == '__main__':
    unittest.main()
