f = open("input.txt", "r")
inputs = f.read()

class Directory:
    def __init__(self, name) -> None:
        self.name = name
        self.path = ''
        self.size = 0
        self.subdirs = []
        self.files = []
        
    def _update_dir(self, name):
        self.subdirs.append(name)

    def _update_file(self, size, name):
        self.files.append(self.path+'/'+name)
        self.size += int(size)

def get_full_path(working_dir):
    if len(working_dir)>2:
        return ''.join(working_dir[:1])+'/'.join(working_dir[1:])
    else:
        return ''.join(working_dir)

def parse_input(inputs):
    directories = {}
    working_dir = []
    instructions = [l for l in inputs.split('\n')]
    for instruction in instructions:
        command = instruction[:4]
        if (command == "$ cd"):
            new_directory = instruction[5:]
            if (new_directory != '..'): 
                working_dir.append(new_directory)
                full_path = get_full_path(working_dir)
                directories[full_path] = Directory(new_directory)
                directories[full_path].path = full_path
            else:
                working_dir.pop()
        elif (command == "$ ls"):
            pass
        else:
            info, name = instruction.split()
            if info == "dir":
                directories[full_path]._update_dir(name)
            else:
                directories[full_path]._update_file(info,name)
                for l in range(len(working_dir)-1,0,-1):
                    parent_path = get_full_path(working_dir[:l])
                    directories[parent_path]._update_file(info,name)
    return directories


directories = parse_input(inputs)

## Part 1
size_small_directories = sum(v.size for k,v in directories.items() if v.size < 100000)

print('The sum of directories with a total size of at most 100000 is : ', size_small_directories)

## Part 2
total_space = 70000000
unused_space = total_space - directories['/'].size
required_space = 30000000 - unused_space
size_smallest_directory = min(v.size for k,v in directories.items() if v.size >= required_space)

print('The size of the smallest directory to erase is : ', size_smallest_directory)
