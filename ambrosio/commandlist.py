

class CommandList(object):
    def __init_(self):
        super(CommandList, self).__init__()
        self.commands = []

    def next(self): #next is the same that get_command
        return self.commands.pop(0) #cua es afegir pel final i desplaçar pel principi FIFO

    def append(self, command):
        self.commands.append(command)

    def length(self):
        return len(self.commands)
