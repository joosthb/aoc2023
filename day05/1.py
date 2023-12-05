
def parsealmanac(almanac: list)-> dict:
    almanacmap = {}
    currentchapter = ''

    for line in almanac:
        if ':' in line:
            if 'map' in line:
                currentchapter = line.split(' map:')[0]
                almanacmap[currentchapter] = {}
            # seeds
            else:
                almanacmap['seeds'] = line.split(': ')[1].split(' ')
        else:
            if line != '':
                dest, source, length = line.split(' ')
                for x in range(int(length)):
                    almanacmap[currentchapter][int(source)+x] = int(dest)+x
    return almanacmap

def mapfunc(almamap, table, id) -> int:
    if id in almamap[table]:
        return almamap[table][id]
    else:
        return id

if __name__ == "__main__":
    with open('input', 'r', encoding="utf-8") as fp:
        lines = fp.read().splitlines()
    almamap = parsealmanac(lines)
    closest = None

    for seed in almamap['seeds']:
        input = int(seed)
        for fromto in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water','water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
            output = mapfunc(almamap, fromto, input)
            input = output
        if closest:
            closest = min(closest, output)
        else:
            closest = output
    print(closest)

    