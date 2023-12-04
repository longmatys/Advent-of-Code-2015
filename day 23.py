import os
from dataclasses import dataclass
from typing import List


@dataclass
class computer():
    a: int
    b: int
    IP: int
    program: List[List[str]]
    def add_instruction(self,ins):
        if self.program[0]:
            self.program.append(ins)
        else:
            self.program = [ins]
    def inc(self,instruction):
        setattr(self, instruction[1], getattr(self,instruction[1]) + 1)
        self.IP += 1
    def jio(self,instruction):
        if getattr(self, instruction[1] ) == 1:
            self.IP += int(instruction[2])
        else:
            self.IP += 1
    def hlf(self,instruction):
        setattr(self, instruction[1], getattr(self,instruction[1]) / 2)
        self.IP += 1
    def jie(self,instruction):
        if getattr(self, instruction[1] ) % 2 == 0:
            self.IP += int(instruction[2])
        else:
            self.IP += 1
    def tpl(self,instruction):
        setattr(self, instruction[1], getattr(self,instruction[1]) * 3)
        self.IP += 1
    def jmp(self,instruction):
        self.IP += int(instruction[1])
    def run(self):
        while self.IP < len(self.program):
            
            current = self.program[self.IP]
            print(current)
            getattr(self, current[0])(current)
            
def main():
    pc = computer(1,0,0,[None])
    # Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip().replace(',','')
            
            
            line_a = line.split(' ')
            #print(line,line_a)
            pc.add_instruction(line_a)
    pc.run()
    print(pc.b)
if __name__ == '__main__':
    main()
