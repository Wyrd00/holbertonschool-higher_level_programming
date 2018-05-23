#/usr/rin/python3
"""

Tests for Base

"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import json

class BaseTest(unittest.TestCase):

    def test_id_normal(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_one_args(self):
        b2 = Base(2)
        self.assertEqual(b2.id, 2)

    def test_id_two_args(self):
        with self.assertRaises(TypeError):
            b3 = Base(89, 2)

    def test_nb(self):
        b = Base(3)
        with self.assertRaises(AttributeError):
            str(b.nb_objects)
        with self.assertRaises(AttributeError):
            str(b.__nb_objects)

    def test_to_json_string(self):
        d1 = {"id": 1, "width": 5, "height": 12, "x": 1, "y": 3}
        d2 = {"id": 3, "width": 6, "height": 3, "x": 8, "y": 2}
        j = Base.to_json_string([d1, d2])
        self.assertFalse(type(j) is list)
        pobj = json.loads(j)
        self.assertEqual(pobj, [d1, d2])
        self.assertTrue(type(pobj) is list)

    def test_from_json_string(self):
        j = '[{"id": 1, "width": 5, "height": 12, "x": 1, "y": 3}, \
            {"id": 3, "width": 6, "height": 3, "x": 8, "y": 2}]'
        dic = Base.from_json_string(j)
        self.assertTrue(type(dic) is list)

    def test_empty_to_json_string(self):
        """Passing empty list"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")
#    def tearDown(self):
 #       self.r1.dispose()
  #      self.r2.dispose()
   #     self.r3.dispose()
    #    self.r4.dispose()
