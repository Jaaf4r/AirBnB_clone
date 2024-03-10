import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()

    def tearDown(self):
        del self.cmd

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("create BaseModel")
            created_id = fake_out.getvalue().strip()
            self.assertTrue(created_id)

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("show BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("destroy BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("all BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "[]")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("update BaseModel")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd("quit"))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.onecmd("")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_eof(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
