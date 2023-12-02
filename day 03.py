import os
import typing
from dataclasses import dataclass,field
from typing import Dict

movement_map = {
    '>': [1,0],
    '<': [-1,0],
    '^': [0,1],
    'v': [0,-1]
}
@dataclass
class town_map_class:
    x: int = 0
    y: int = 0
    robo_x: int = 0
    robo_y: int = 0
    santa_move: bool = True
    local_map: Dict[int,Dict[int,int]] = field(default_factory = lambda:( {0:{0:0}}))
    house_counter:int = 0
    def move(self, direction):
        if self.santa_move:
            self.x += direction[0]
            self.y += direction[1]
            x = self.x
            y = self.y
        else:
            self.robo_x += direction[0]
            self.robo_y += direction[1]
            x = self.robo_x
            y = self.robo_y
        self.santa_move = not self.santa_move
        if self.local_map.get(x):
            if self.local_map.get(x).get(y):
                self.local_map[x][y] += 1
            else:
                self.house_counter += 1
                self.local_map[x][y] = 1
        else:
            self.house_counter += 1
            self.local_map[x] = {y: 1}
        

    
if __name__ == '__main__':
    # Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    town_map = town_map_class()
    town_map.move([0,0])
    print(town_map)
    with open(input_file) as f:
        retez = f.readline()
        retez.strip()
                
        for znak in retez:
            
            town_map.move(movement_map[znak])
            
    print(town_map.house_counter)
            