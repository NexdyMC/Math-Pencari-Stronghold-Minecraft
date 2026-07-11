import math
# import argv

pointA = "/execute in minecraft:overworld run tp @s 1000.50 87.49 1000.50 -111.13 -31.93"
pointB = "/execute in minecraft:overworld run tp @s 996.70 83.00 890.30 -81.68 -32.27"

# /execute in minecraft:overworld run tp @s 1000.50 87.49 1000.50 -111.13 -31.93
# /execute in minecraft:overworld run tp @s 996.70 83.00 890.30 -81.68 -32.27

dataA = pointA.split()
dataB = pointB.split()

# print(dataA[6], dataA[8], dataA[9])
# print(dataB[6], dataB[8], dataB[9])

poinxA = int(float(str(dataA[6])))
poinzA = int(float(str(dataA[8])))
angleA = float(str(dataA[9]))

poinxB = int(float(str(dataB[6])))
poinzB = int(float(str(dataB[8])))
angleB = float(str(dataB[9]))

print(f"poin A: {poinxA} {poinzA} {angleA}")
print(f"poin B: {poinxB} {poinzB} {angleB}")

class rumus():
    def coord(poinxA, poinzA, angleA, poinxB, poinzB, angleB):
        
        deg2rad = math.pi / 180
        rad2deg = 180 / math.pi

        if angleA >= 90:
            hasilA = (180 - angleA) + 90
        else:
            hasilA = -1 * (angleA + 90)
        # print(hasilA)

        if angleB >= 90:
            hasilB = (180 - angleB) + 90
        else:
            hasilB = -1 * (angleB + 90)
        # print(hasilB)

        clopeA = -1 * math.tan(hasilA * deg2rad)
        clopeB = -1 * math.tan(hasilB * deg2rad)

        # print(f"{clopeA}, {clopeB}")
        interceptA = poinzA - clopeA * poinxA
        interceptB = poinzB - clopeB * poinxB

        # print(f"{interceptA}, {interceptB}")

        X = (interceptB - interceptA) / (clopeA - clopeB)
        Z = (clopeA * X) + interceptA
        return math.floor(X), math.floor(Z)

    def overword_block(coordX, coordZ):
        return "Overword Block: ", math.floor(coordX), math.floor(coordZ)

    def overword_chunk(coordX, coordZ):
        return "Overword Chunk: ", math.floor(coordX / 16), math.floor(coordZ / 16)

    def nether_block(coordX, coordZ):
        return "Nether Block: ", math.floor(coordX / 8), math.floor(coordZ / 8)
    
    def nether_chunk(coordX, coordZ):
        return "Nether Chunk: ", math.floor((coordX / 8) / 16), math.floor((coordZ / 8) / 16)

def calcurator_stronghold(poinxA, poinzA, angleA, poinxB, poinzB, angleB):
    deg2rad = math.pi / 180
    rad2deg = 180 / math.pi

    if angleA >= 90:
        hasilA = (180 - angleA) + 90
    else:
        hasilA = -1 * (angleA + 90)
    # print(hasilA)

    if angleB >= 90:
        hasilB = (180 - angleB) + 90
    else:
        hasilB = -1 * (angleB + 90)
    # print(hasilB)

    clopeA = -1 * math.tan(hasilA * deg2rad)
    clopeB = -1 * math.tan(hasilB * deg2rad)

    # print(f"{clopeA}, {clopeB}")
    interceptA = poinzA - clopeA * poinxA
    interceptB = poinzB - clopeB * poinxB

    # print(f"{interceptA}, {interceptB}")

    X = (interceptB - interceptA) / (clopeA - clopeB)
    Z = (clopeA * X) + interceptA
    return X, Z

# def output():
#     return 123, 123

# kelas = rumus.coord(poinxA, poinzA, angleA, poinxB, poinzB, angleB)
# chunk = rumus.overword_chunk(kelas[0], kelas[1])
# print(chunk)

# hasil = calcurator_stronghold(poinxA, poinzA, angleA, poinxB, poinzB, angleB)
# print(hasil[0], hasil[1])

# print(f"Overword Block: {math.floor(X)}, {math.floor(Z)}")
# print(f"Overword Chunk: {math.floor(X / 16)}, {math.floor(Z / 16)}")

# print(f"Nether Block: {math.floor(X / 8)}, {math.floor(Z / 8)}")
# print(f"Nether Chunk: {math.floor((X / 16) / 8)}, {math.floor((Z / 16) / 8)}")