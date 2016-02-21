# Complex parts
class CPU:
    def __init__(self): pass
    def freeze(self): pass
    def jump(self, position): pass
    def execute(self): pass

class Memory:
    def __init__(self): pass
    def load(self, position, data): pass

class HardDrive:
    def __init__(self): pass
    def read(self, lba, size): pass

# Facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start_computer(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(0, 1024))
        self.cpu.jump(10)
        self.cpu.execute()

# Client
if __name__ == '__main__':
    facade = Computer()
    facade.start_computer()
