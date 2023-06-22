def parse_input(input_path: str) -> list[tuple[str, int]]:
    with open(input_path, 'r') as f:
        commands = f.read().strip().split('\n')
        commands = [(comm.split()[0], int(comm.split()[1])) for comm in commands]
        return commands

def part1(data: list[tuple[str, int]]) -> int:
    pos = (0, 0)
    for comm in data:
        if comm[0] == 'down':
            pos = (pos[0], pos[1] + comm[1])
        elif comm[0] == 'up':
            pos = (pos[0], pos[1] - comm[1])
        else:
            pos = (pos[0] + comm[1], pos[1])
    return pos[0] * pos[1]

def part2(data: list[tuple[str, int]]) -> int:
    pos = (0, 0)
    aim = 0
    for comm in data:
        if comm[0] == 'down':
            aim += comm[1]
        elif comm[0] == 'up':
            aim -= comm[1]
        else:
            pos = (pos[0] + comm[1], pos[1] + aim * comm[1])            
    return pos[0] * pos[1]

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day02.txt')))
    print ('Part Two:', part2(parse_input('input/day02.txt')))
