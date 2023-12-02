from dataclasses import dataclass
@dataclass
class darek:
    l: int
    w: int
    h: int
    def wrap_size(self) -> int:
        #print(2*self.l*self.w , 2*self.w*self.h , 2*self.h*self.l , sorted([self.l*self.w , self.w*self.h , self.h*self.l]))
        return 2*self.l*self.w + 2*self.w*self.h + 2*self.h*self.l + min(self.l*self.w , self.w*self.h , self.h*self.l)
    def ribbon_len(self) -> int:
        rib = sorted([self.l , self.w , self.h])
        rib_size = 2*rib[0]+2*rib[1] + rib[0]*rib[1]*rib[2]
        
        return rib_size
    def __init__(self,retez) -> None:
        test_a = retez.split('x')
        self.l = int(test_a[0])
        self.w = int(test_a[1])
        self.h = int(test_a[2])
    
if __name__ == '__main__':
    paper = 0
    ribbon = 0
    with open("day 02.input.txt") as f:
        for line in f.readlines():
            line.strip()
            local_darek = darek(line)
            paper+=local_darek.wrap_size()
            ribbon += local_darek.ribbon_len()
    print(paper,ribbon)
    
    #local_darek = darek('2x3x4')
    #print(local_darek,local_darek.ribbon_len())
    