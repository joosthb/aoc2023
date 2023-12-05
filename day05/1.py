class Almanac:
    _map = {}
    _seeds = []

    def __init__(self, source: list[str]):
        currentchapter = ''
        for line in source:
            if ':' in line:
                if 'map' in line:
                    currentchapter = line.split(' map:')[0]
                    self._map[currentchapter] = {}
                # seeds
                else:
                    self._seeds = [int(seed) for seed in line.split(': ')[1].split(' ')]
            else:
                if line != '':
                    dest, source, length = line.split(' ')
                    for x in range(int(length)):
                        self._map[currentchapter][int(source)+x] = int(dest)+x
    @property
    def seeds(self) -> list[int]:
        return self._seeds

    @property
    def map(self) -> dict:
        return self._map

def mapfunc(almamap, table, id) -> int:
    if id in almamap[table]:
        return almamap[table][id]
    else:
        return id

if __name__ == "__main__":
    with open('testinput', 'r', encoding="utf-8") as fp:
        lines = fp.read().splitlines()
    almanac = Almanac(lines)
    print(almanac.map)
    print(almanac.seeds)

    # # closest = None
    # for seed in almamap['seeds']:
    #     input = int(seed)
    #     for fromto in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water','water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
    #         output = mapfunc(almamap, fromto, input)
    #         input = output
    #     if closest:
    #         closest = min(closest, output)
    #     else:
    #         closest = output
    # print(closest)
