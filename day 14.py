import os
if __name__ == '__main__':
# Get the name of the Python script
    script_name = os.path.basename(__file__)
    input_file = script_name.split('.')[0]+'.input.txt'
    output_wires = {}
    nodes = {}
    edges = {}
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            
