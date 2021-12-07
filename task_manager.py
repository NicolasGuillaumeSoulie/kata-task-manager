import unittest

def add(tasks, desc):
	lastId = 1 if len(tasks)<1 else max(tasks.keys())
	tasks[lastId] = Task(desc)

def remove(tasks, id):
	print(int(id))
	del tasks[int(id)]

def done(tasks, id):
	tasks[int(id)].status = "done"

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

class Task:
	def __init__(self, desc):
		self.desc = desc
		self.status = "to do"

class TaskManager:
	def __init__(self):
		self.tasks = {}

	def cmd(self, inValue = input):
		inCmd = inValue()
		parser[inCmd[0]](self.tasks, inCmd[2::])

class TestTaskManager(unittest.TestCase):

    def test_parsing_add(self):
        self.assertEqual(parser['+'], add)

    def test_parsing_remove(self):
        self.assertEqual(parser['-'], remove)

    def test_parsing_done(self):
        self.assertEqual(parser['x'], done)

    def test_parsing_toDo(self):
        self.assertEqual(parser['o'], toDo)

    def test_parsing_Quit(self):
        self.assertEqual(parser['q'], quit)

    def test_addTask(self):
    	tm = TaskManager()
    	tm.cmd(lambda : "+ Learn Python")
    	self.assertEqual(tm.tasks[1].desc, "Learn Python")

    def test_removeTask(self):
    	tm = TaskManager()
    	tm.cmd(lambda : "+ Learn Python")
    	tm.cmd(lambda : "- 1")
    	self.assertEqual(len(tm.tasks), 0)

    def test_done(self):
    	tm = TaskManager()
    	tm.cmd(lambda : "+ Learn Python")
    	tm.cmd(lambda : "x 1")
    	self.assertEqual(tm.tasks[1].status, "done")


if __name__ == '__main__':
    unittest.main()