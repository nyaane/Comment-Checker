import config

def __read__(fn):
    output = []
    with open(fn, "r") as input_file:
        for line in input_file:
            line = line.strip()
            if (len(line) > 0):
                output.append(line)
    return output

def __write__(fn, data):
    with open(fn, "w") as output_file:
        for line in data:
            output_file.write(line + "\n")

def readDead():
    return __read__(config.dead_file)

def readLive():
    return __read__(config.live_file)

def writeDead(data):
    __write__(config.dead_file, data)

def writeLive(data):
    __write__(config.live_file, data)
