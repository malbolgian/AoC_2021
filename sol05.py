import re

class LineSeg:
    def __init__(self, coords: list[int]):
        self.p1 = (coords[0], coords[1])
        self.p2 = (coords[2], coords[3])
        # Order tuples to make it easier down the lines
        if self.p2 < self.p1:
            self.p1, self.p2 = self.p2, self.p1

    def find_lattice(self, part1: bool) -> set[tuple[int, int]]:
        # Handles horizontal + vertical lines
        points = set()
        if self.p1[0] == self.p2[0]:
            for y in range(self.p1[1], self.p2[1] + 1):
                points.add((self.p1[0], y))
        if self.p1[1] == self.p2[1]:
            for x in range(self.p1[0], self.p2[0] + 1):
                points.add((x, self.p1[1]))
        if len(points) > 0 or part1:
            return points
        # Handles diagonal lines
        y_dir = 1 if self.p2[1] > self.p1[1] else -1
        for inc in range(self.p2[0] - self.p1[0] + 1):
            points.add((self.p1[0] + inc, self.p1[1] + y_dir * inc))
        return points

def parse_input(input_path: str) -> list[LineSeg]:
    with open(input_path, 'r') as f:
        segments = f.read().strip().split('\n')
        lines = []
        for seg in segments:
            coords = [int(n) for n in re.findall('\d+', seg)]
            lines.append(LineSeg(coords))
        return lines

def part1(data: list[LineSeg]) -> int:
    point_counter = dict()
    for seg in data:
        for p in seg.find_lattice(part1 = True):
            point_counter[p] = point_counter.get(p, 0) + 1
    return sum(1 for freq in point_counter.values() if freq > 1)

def part2(data: list[LineSeg]) -> int:
    point_counter = dict()
    for seg in data:
        for p in seg.find_lattice(part1 = False):
            point_counter[p] = point_counter.get(p, 0) + 1
    return sum(1 for freq in point_counter.values() if freq > 1)

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day05.txt')))
    print ('Part Two:', part2(parse_input('input/day05.txt')))
