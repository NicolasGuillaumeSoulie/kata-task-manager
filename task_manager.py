import unittest

def add():
	return 

def remove():
	return

def done():
	return

def toDo():
	return

def quit():
	return

parser = {
	"+" : add,
	"-" : remove,
	"x" : done,
	"o" : toDo,
	"q" : quit
}

class cmd:

	def __init__(self, string):
		self.taskName = string[2::]
		self.cmd = parser[string[0]]
		

class TestTaskManager(unittest.TestCase):

    def test_parsing_add(self):
        self.assertEqual(cmd('+ Learn Python').cmd, add)

    def test_parsing_remove(self):
        self.assertEqual(cmd('- 1').cmd, remove)

    def test_parsing_done(self):
        self.assertEqual(cmd('x 1').cmd, done)

    def test_parsing_done(self):
        self.assertEqual(cmd('o 1').cmd, toDo)

    def test_parsing_done(self):
        self.assertEqual(cmd('q').cmd, quit)

if __name__ == '__main__':
    unittest.main()