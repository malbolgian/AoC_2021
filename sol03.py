def parse_input(input_path: str) -> list[str]:
    with open(input_path, 'r') as f:
        nums = f.read().strip().split('\n')
        return nums

def part1(data: list[str]) -> int:
    N = len(data[0])
    gamma = ''
    for i in range(N):
        bits = [num[i] for num in data]
        gamma += ('1' if bits.count('1') > bits.count('0') else '0')
    gamma = int(gamma, base = 2)
    return gamma * (2 ** N - 1 - gamma)

def o2_crit(nums: list[str], ind: int) -> list[str]:
    bits = [num[ind] for num in nums]
    bit_crit = '1' if bits.count('1') >= len(nums) / 2 else '0'
    return list(filter(lambda s: s[ind] == bit_crit, nums))

def co2_crit(nums: list[str], ind: int) -> list[str]:
    bits = [num[ind] for num in nums]
    bit_crit = '0' if bits.count('0') <= len(nums) / 2 else '1'
    return list(filter(lambda s: s[ind] == bit_crit, nums))

def part2(data: list[str]) -> int:
    i = 0
    o2_rating = data[:]
    while len(o2_rating) > 1:
        o2_rating = o2_crit(o2_rating, i)
        i += 1
    
    i = 0
    co2_rating = data[:]
    while len(co2_rating) > 1:
        co2_rating = co2_crit(co2_rating, i)
        i += 1

    return int(o2_rating[0], base = 2) * int(co2_rating[0], base = 2)

if __name__ == '__main__':
    print ('Part One:', part1(parse_input('input/day03.txt')))
    print ('Part Two:', part2(parse_input('input/day03.txt')))
