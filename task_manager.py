import unittest

def add():
	return 

parser = {
	"+" : add
}

class cmd:

	def __init__(self, string):
		self.taskName = string[2::]
		self.cmd = parser[string[0]]
		

class TestTaskManager(unittest.TestCase):

    def test_parsing_add(self):
        self.assertEqual(cmd('+ Learn Python').cmd, add)

if __name__ == '__main__':
    unittest.main()