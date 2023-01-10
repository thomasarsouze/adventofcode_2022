f = open("input.txt", "r")
inputs = f.read()

def parse_input(inputs):
    signal = [] 
    for l in inputs.split('\n'):
        print(l)
        if (l == 'noop'):
            signal.append((l,0))
        else:
            c, v = l.split()
            signal.append((c, int(v)))
            
    return signal

def execute_program(c,v):
    if c == "noop":
        x.append(x[-1])
    else:
        x.append(x[-1])
        x.append(x[-1]+v)
    
signal = parse_input(inputs)

## Part 1
x = [1]
for c,v in signal:
    execute_program(c,v)

print("Nb of visible trees : ", sum([i*x[i-1] for i in [20, 60, 100, 140, 180, 220]]))

## Part 2
crt = ['#' if x[i] in [(i-1)%40,i%40,(i+1)%40] else '.' for i in range(240)]    
for i in range(0, 240, 40):
    print("".join(crt[i : i + 40]))
    
