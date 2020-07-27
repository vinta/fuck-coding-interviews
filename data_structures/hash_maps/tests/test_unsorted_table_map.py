# coding: utf-8
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
        self.map[self.d3['key']] = self.d3['value']
        self.dict[self.d3['key']] = self.d3['value']
        self.assertCountEqual(list(self.map), list(self.dict))

    def test__getitem__(self):
        self.assertEqual(self.map[self.d1['key']], self.dict[self.d1['key']])
        self.assertEqual(self.map[self.d2['key']], self.dict[self.d2['key']])

    def test__delitem__(self):
        del self.map[self.d1['key']]
        del self.dict[self.d1['key']]
        self.assertCountEqual(list(self.map), list(self.dict))


if __name__ == '__main__':
    unittest.main()
