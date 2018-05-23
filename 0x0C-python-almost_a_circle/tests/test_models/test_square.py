#/usr/bin/python3
"""

Tests for Square

"""
import unittest
import json
import sys
from io import StringIO
from models.square import Square
from models.base import Base


class SquareTest(unittest.TestCase):

    def setUp(self):
        self.r1 = Square(2, 4)
        self.r2 = Square(5, 10, 2)
        self.r3 = Square(3, 6, 2)
        self.r4 = Square(10, 7, 1, 7)

    def test_id(self):
        self.assertEqual(self.r4.id, 7)

    def test_width(self):
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r3.width, 3)
        self.assertEqual(self.r4.width, 10)

    def test_height(self):
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 5)
        self.assertEqual(self.r3.height, 3)
        self.assertEqual(self.r4.height, 10)

    def test_x(self):
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r2.x, 10)
        self.assertEqual(self.r3.x, 6)
        self.assertEqual(self.r4.x, 7)

    def test_y(self):
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 2)
        self.assertEqual(self.r3.y, 2)
        self.assertEqual(self.r4.y, 1)

    def test_size_missing(self):
        with self.assertRaises(TypeError):
            r10 = Square()

    def test_size_TypeError(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r10 = Square('five')

    def test_size_ValueError(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r10 = Square(-5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r10 = Square(0, 2)

    def test_x_TypeError(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r10 = Square(2, "x")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r10 = Square(1, [[12]])

    def test_x_ValueError(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r10 = Square(2, -5)

    def test_y_TypeError(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r10 = Square(2, 3, (12, 1))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(2, 3, [{'keykey': 'haha'}])

    def test_y_ValueError(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r10 = Square(2, 3, -10)

    def test_area(self):
        self.assertEqual(self.r1.area(), 4)
        self.assertEqual(self.r2.area(), 25)
        self.assertEqual(self.r3.area(), 9)
        self.assertEqual(self.r4.area(), 100)

    def test_area_unnecessary_arg(self):
        with self.assertRaises(TypeError):
            self.r1.area(12)

    def display(self):
        s = Square(1, 1, 1, 1)
        var = StringIO()
        sys.stdout = var
        r.display()
        self.assertEquals(var.getvalue(), '#\n')
        sys.stdout = sys.__stdout__

    def update_arg(self):
        """normal condition for updating"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (4) 2/3 - 1')
        s.update(11)
        self.assertEqual(str(s), "[Square] (11) 2/3 - 1")
        s.update(11, 22)
        self.assertEqual(str(s), "[Square] (11) 2/3 - 22")
        s.update(11, 22, 33)
        self.assertEqual(str(s), "[Square] (11) 33/3 - 22")
        s.update(11, 22, 33, 44)
        self.assertEqual(str(s), "[Square] (11) 33/44 - 22")

    def test_update_args_empty(self):
        """update empty parameter with arg update"""
        s = Square(4, 2, 1, 0)
        s.update()
        self.assertEqual(str(s), '[Square] (0) 2/1 - 4')

    def test_update_args_TypeError(self):
        """typeerror with arg update"""
        r = Square(4, 2, 1, 0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "bobobum")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(2, 1, [['34']])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, {"potato": "pohtato"})

    def test_update_args_ValueError(self):
        """value error w/arg update"""
        r = Square(4, 2, 1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(2, -7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(7, 8, -7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(10, 1, 3, -7)

    def test_kwargs(self):
        """test kwarg works in normal conditions"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=100)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 100")
        s.update(size=11, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 11")
        s.update(y=3, x=5, id=9)
        self.assertEqual(str(s), "[Square] (9) 5/3 - 11")

    def test_kwargs_new_key(self):
        """non-existant key w/kwarg in instance"""
        r10 = Square(4, 2, 1, 0)
        r10.update(jigglypuff=30)
        self.assertEqual(r10.jigglypuff, 30)

    def test_update_kwargs_TypeError(self):
        """type error for kwargs update"""
        r = Square(4, 2, 1, 0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(size="bobobum")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x=[['34']])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y={"potato": "pohtato"})

    def test_update_kwargs_ValueError(self):
        """value error for kwargs update"""
        r = Square(4, 2, 1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(size=0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(size=-7)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-7)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-7)

    def to_dict(self):
        """check that to_dictionary work"""
        d1 = self.r1.to_dictionary()
        self.assertTrue(isinstance(d1, dict))

    def to_dictionary_update(self):
        """check update for dict works"""
        s5 = (100, 120, 40, 10)
        d5 = self.s5.to_dictionary()
        r = Square(11, 22, 33, 44)
        r.update(**d5)
        self.assertEqual(r.__dict__, d5)

    def create_square(self):
        """test normal use of create"""
        s = {"id": 1, "size": 2, "x": 1, "y": 1}
        new_s = Rectangle.create(**s)
        self.assertEqual(str(new_s), "[Square] (1) 1/1 - 2")

    def test_save_to_file(self):
        """save_to_file under normal conditions"""
        r11 = Square(1, 2, 3, 4)
        r12 = Square(11, 22, 33, 44)
        pobj = [r11, r12]
        Square.save_to_file(pobj)
        with open("Square.json", "r", encoding='utf-8') as f:
            ls = [r11.to_dictionary(), r12.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_save_to_file_empty(self):
        """save_to_file with empty list"""
        tehe = []
        Square.save_to_file(tehe)
        with open("Square.json", "r", encoding='utf-8') as f:
            self.assertEqual("[]", f.read())

    def test_load_from_file(self):
        """load_from_file under normal conditions"""
        r01 = Square(1, 2, 3, 4)
        r02 = Square(11, 22, 33, 44)
        pobj = [r01, r02]
        Square.save_to_file(pobj)
        hiya = Square.load_from_file()
        self.assertEqual(type(hiya), list)
