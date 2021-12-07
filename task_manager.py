import unittest

def add():
	return 

def remove():
	return

parser = {
	"+" : add,
	"-" : remove
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

if __name__ == '__main__':
    unittest.main()