#!python3
from helpers import iter_input, iter_test

program = []
for line in iter_input(8):
    program.append(line)


class interpreter():

    def __init__(self):

        self._accumulator = 0
        self.program = False

    def loadProgram(self, program):
        self._currentLine = 0
        self.program = program
        self._programLength = len(self.program)

    def run(self, command=None):
        if self.program:
            self.linesrun = []
            while self._currentLine < self._programLength:
                self._runCommand(self.program[self._currentLine])
        elif command:
            self._runCommand(command)
        else:
            raise SyntaxError("No command to run.")

    def _runCommand(self, command):
        if self.program:
            if self._currentLine in self.linesrun:
                raise RuntimeError(f"Operation not allowed. Dumping State.\n"
                                   f"Line: {self._currentLine} AccVal: {self._accumulator}")
            self.linesrun.append(self._currentLine)

        cmd, val = command.split()
        if cmd not in ["acc", "jmp", "nop"]:
            raise SyntaxError(f"{cmd}: command not recognized")
        eval(f"self.{cmd}(int(val))")

    def acc(self, val):
        self._accumulator += val
        if self.program:
            self._currentLine += 1

    def jmp(self, val):
        if self.program:
            self._currentLine += val
            if self._currentLine < 0:
                self._currentLine = 0

    def nop(self, val):
        if self.program:
            self._currentLine += 1


interp = interpreter()
interp.loadProgram(program)
interp.run()
