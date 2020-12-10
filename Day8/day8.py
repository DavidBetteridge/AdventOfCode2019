image = open('Day8/day8.txt').read()
layerSize = 25 * 6
layers = [image[i:i+layerSize] for i in range(0, len(image), layerSize)]

def part_one():
    zeros = [ (layer.count('0'), index) for index, layer in enumerate(layers)]
    _, layerNumber = min(zeros)
    return layers[layerNumber].count('1') * layers[layerNumber].count('2')

def part_two():
    result = ""
    for r in range(0,6):
        row = ""
        for c in range(0, 25):
            offset = c + (r * 25)
            row += next(iter([layer[offset] for layer in layers if layer[offset] != '2']))
        result = result + row.replace('0', ' ') + '\r\n'
    return result        