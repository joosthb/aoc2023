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
            if map[1] < sourceid < (map[1] + map[2]):
                return sourceid - map[1] + map[0]
        return sourceid
    
    def seedtolocation(self, seedid: int) -> int:
        input = seedid
        for fromto in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water','water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
            output = self._sourcetodest(fromto, input)
            input = output
        return output


if __name__ == "__main__":
    with open('input', 'r', encoding="utf-8") as fp:
        lines = fp.read().splitlines()
    almanac = Almanac(lines)
    locations = [almanac.seedtolocation(seed) for seed in almanac.seeds]
    print(f'Shortest route from seed to location: %d' % min(locations))
