import unittest
import sys, os.path

app_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/main/')
sys.path.append(app_dir)
import routes
#sys.path.insert(0,'c:/Users/osama/Desktop/docker_project/hello_docker/main/')
#from main import app

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(routes.hello_world(), "<p>Hello, World!</p>")

    def test_name(self):
        self.assertEqual(routes.name("osama"), "<p>Hello, osama </p>")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()