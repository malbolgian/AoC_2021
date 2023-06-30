def parse_input(input_path: str) -> list[int]:
    # Returns frequencies of internal timers rather than un-processed timers
    with open(input_path, 'r') as f:
        x = f.read()
        return [x.count(str(i)) for i in range(9)]

def step(freq: list[int]) -> list[int]:
    # Count down each internal timer, convert all 0s to a 6 and an 8
    new_freq = freq[1:]
    new_freq.append(freq[0])
    new_freq[6] += freq[0]
    return new_freq

def part1(data: list[int]) -> int:
    DAYS = 80
    for i in range(DAYS):
        data = step(data)
    return sum(data)

def part2(data: list[int]) -> int:
    DAYS = 256
    for i in range(DAYS):
        data = step(data)
    return sum(data)

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day06.txt')))
    print ('Part Two:', part2(parse_input('input/day06.txt')))
