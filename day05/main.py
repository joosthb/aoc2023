from functools import cached_property 

class Almanac:
    _map = {}
    _seeds = []

    def __init__(self, source: list[str]):
        currentchapter = ''
        for line in source:
            if ':' in line:
                if 'map' in line:
                    currentchapter = line.split(' map:')[0]
                    self._map[currentchapter] = []
                # seeds
                else:
                    self._seeds = [int(seed) for seed in line.split(': ')[1].split(' ')]
            else:
                if line != '':
                    # dest, source, length
                    self._map[currentchapter] += [[int(x) for x in line.split(' ')]]

    @cached_property
    def seedranges(self)-> list[tuple[int, int]]:
        seedsranges: list[tuple[int, int]] = []
        for i in range(int(len(self._seeds))):
            if i%2:
                seedsranges.append((self._seeds[i-1], self._seeds[i]))
        return seedsranges
    
    @cached_property
    def rangemaps(self):
        ''' eats map and creates list of rangerules: from, to, rule'''
        rulemap = []
        for x, map in enumerate(self._map):
            # rulemap[x] = []
            # seeds needed
            if x == 0:
                for seedrange in self.seedranges:
                    for rule in self._map[map]:
                        print(rule)
            else:
                print(x, self._map[map])

    @property
    def seeds(self) -> list[int]:
        return self._seeds

    @property
    def map(self) -> dict:
        return self._map

    def _sourcetodest(self, chapter: str, sourceid: int) -> int:
        '''
        Function to map source id to destination id using almanac chapter map
        '''
        for map in self._map[chapter]:
            if map[1] <= sourceid <= (map[1] + map[2]):
                return sourceid - map[1] + map[0]
        return sourceid
    
    def seedtolocation(self, seedid: int) -> int:
        input = seedid
        for fromto in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water','water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
            output = self._sourcetodest(fromto, input)
            input = output
        return output


if __name__ == "__main__":
    with open('testinput', 'r', encoding="utf-8") as fp:
        lines = fp.read().splitlines()
    almanac = Almanac(lines)
    # Part 1
    locations = [almanac.seedtolocation(seed) for seed in almanac.seeds]
    print(f'Part1, Shortest route from seed to location: %d' % min(locations))

    print(almanac.seedranges)
    print(almanac.map)
    print(almanac.rangemaps)

    exit()

    # Part 2
    lowest = None
    for i, seed in enumerate(almanac.seeds):
        if i%2:
            j = almanac.seeds[i-1]
            while j < seed+almanac.seeds[i-1]:
                if lowest:
                    lowest = min(almanac.seedtolocation(j), lowest)
                else:
                    lowest = almanac.seedtolocation(j)
                j += 1

    print(f'Part2, Shortest route from seed to location: %d' % lowest)