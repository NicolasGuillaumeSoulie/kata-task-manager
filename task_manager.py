import unittest

def add(tasksMan, desc):
	lastId = 1 if len(tasksMan.tasks)<1 else max(tasksMan.tasks.keys()) + 1
	tasksMan.tasks[lastId] = Task(lastId, desc)

def remove(tasksMan, id):
	print(int(id))
	del tasksMan.tasks[int(id)]

def done(tasksMan, id):
	tasksMan.tasks[int(id)].status = "done"

def toDo(tasksMan, id):
	tasksMan.tasks[int(id)].status = "to do"

def quit(tasksMan, osef):
	tasksMan.exit = True

parser = {
	"+" : add,
	"-" : remove,
	"x" : done,
	"o" : toDo,
	"q" : quit
}

class Task:
	def __init__(self, idNum, desc):
		self.id = idNum
		self.desc = desc
		self.status = "to do"

	def toString(self):
		done = " " if self.status == "to do" else "x"
		return "{0} [{1}] {2}".format(self.id, done ,self.desc)

class TaskManager:
	def __init__(self):
		self.tasks = {}
		self.exit = False

	def cmd(self, inValue = input):
		inCmd = inValue()
		parser[inCmd[0]](self, inCmd[2::])

	def display(self):
		cmdString = ""
		for task in self.tasks.values():
			cmdString += task.toString() + "\n"
		return cmdString

	def loop(self, inValues = input):
		self.exit = False 
		while not self.exit:
			self.cmd(inValues)
			print(self.display())

fakeInputs = ["+ Learn Python", "+ Learn TDD", "+ Learn SQL", "x 2", "q"]

def fakeConsole():
	fakeIn = fakeInputs[0] + ""
	del fakeInputs[0]
	print(fakeIn)
	return fakeIn

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

    def test_toDo(self):
    	tm = TaskManager()
    	tm.cmd(lambda : "+ Learn Python")
    	tm.cmd(lambda : "x 1")
    	tm.cmd(lambda : "o 1")
    	self.assertEqual(tm.tasks[1].status, "to do")

    def test_displayTaskToDo(self):
    	tm = TaskManager()
    	tm.cmd(lambda : "+ Learn Python")
    	self.assertEqual(tm.tasks[1].toString(), "1 [ ] Learn Python")

    def test_displayTaskDone(self):
    	tm = TaskManager()
    	tm.cmd(lambda : "+ Learn Python")
    	tm.cmd(lambda : "x 1")
    	self.assertEqual(tm.tasks[1].toString(), "1 [x] Learn Python")

    def test_displayAllTasks(self):
    	tm = TaskManager()
    	tm.cmd(lambda : "+ Learn Python")
    	tm.cmd(lambda : "+ Learn TDD")
    	tm.cmd(lambda : "+ Learn SQL")
    	self.assertEqual(tm.display(), "1 [ ] Learn Python\n2 [ ] Learn TDD\n3 [ ] Learn SQL\n")

    def test_loop(self):
    	tm = TaskManager()
    	tm.loop(fakeConsole)
    	self.assertEqual(tm.display(), "1 [ ] Learn Python\n2 [x] Learn TDD\n3 [ ] Learn SQL\n")

if __name__ == '__main__':
    unittest.main()