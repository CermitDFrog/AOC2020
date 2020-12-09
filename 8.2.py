#!python3
from helpers import iter_input, iter_test

program = []
for line in iter_input(8):
    program.append(line)


class interpreter():

    def __init__(self):

        self.program = False
        self._accumulator = 0

    def loadProgram(self, program):
        self.program = program
        self._programLength = len(self.program)

    def run(self, command=None):
        if self.program:
            self._currentLine = 0
            self._accumulator = 0
            self.linesrun = []
            while self._currentLine < self._programLength:
                self._runCommand(self.program[self._currentLine])
            print(self._accumulator)
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

    def debugProgram(self, program):

        self.loadProgram(program)
        replaced = []
        try:
            self.run()
        except RuntimeError:
            origlinesrun = self.linesrun.copy()
            for line in reversed(origlinesrun):
                if line in replaced:
                    continue
                if "nop" in self.program[line]:
                    self.program[line] = self.program[line].replace("nop", "jmp")
                    try:
                        self.run()
                    except RuntimeError:
                        continue
                    else:
                        break
                if "jmp" in self.program[line]:
                    self.program[line] = self.program[line].replace("jmp", "nop")
                    try:
                        self.run()
                    except RuntimeError:
                        continue
                    else:
                        break


interp = interpreter()
interp.debugProgram(program)
