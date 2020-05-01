import unittest

import minidl


class TestModel(unittest.TestCase):
    def test_init(self):
        model = minidl.Model()
        self.assertEqual(True, True)


class TestOperator(unittest.TestCase):
    def test_init(self):
        op = minidl.Operator()
        op = minidl.IdentityOp()


class TestTensor(unittest.TestCase):
    def test_init(self):
        t = minidl.Tensor()


if __name__ == '__main__':
    unittest.main()
