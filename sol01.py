def parse_input(input_path: str) -> list[int]:
    with open(input_path, 'r') as f:
        depths = [int(num) for num in f.read().strip().split('\n')]
        return depths

def part1(data: list[int]) -> int:
    return sum(nex > pre for nex, pre in zip(data[1:], data[:-1]))

def part2(data: list[int]) -> int:
    # Adjacent three-measurement sliding window sums contain two elements in common, only outside measurements need to be compared
    return sum(nex > pre for nex, pre in zip(data[3:], data[:-3]))

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day01.txt')))
    print ('Part Two:', part2(parse_input('input/day01.txt')))
