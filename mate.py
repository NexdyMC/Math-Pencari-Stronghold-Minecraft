import math
# import argv

pointA = "/execute in minecraft:overworld run tp @s 1000.50 87.49 1000.50 -111.13 -31.93"
pointB = "/execute in minecraft:overworld run tp @s 996.70 83.00 890.30 -81.68 -32.27"

dataA = pointA.split()
dataB = pointB.split()
print(dataA[6], dataA[8], dataA[9])
print(dataB[6], dataB[8], dataB[9])

poinxA = int(float(str(dataA[6])))
poinzA = int(float(str(dataA[8])))
angleA = float(str(dataA[9]))

poinxB = int(float(str(dataB[6])))
poinzB = int(float(str(dataB[8])))
angleB = float(str(dataB[9]))

print(f"{poinxA} {poinzA} {angleA}")
print(f"{poinxB} {poinzB} {angleB}")

deg2rad = math.pi / 180
rad2deg = 180 / math.pi

if angleA >= 90:
    hasilA = (180 - angleA) + 90
else:
    hasilA = -1 * (angleA + 90)
print(hasilA)

if angleB >= 90:
    hasilB = (180 - angleB) + 90
else:
    hasilB = -1 * (angleB + 90)
print(hasilB)

clopeA = -1 * math.tan(hasilA * deg2rad)
clopeB = -1 * math.tan(hasilB * deg2rad)

print(f"{clopeA}, {clopeB}")
interceptA = poinzA - clopeA * poinxA
interceptB = poinzB - clopeB * poinxB

print(f"{interceptA}, {interceptB}")

X = (interceptB - interceptA) / (clopeA - clopeB)
Z = (clopeA * X) + interceptA

print(f"Overword Block: {math.floor(X)}, {math.floor(Z)}")
print(f"Overword Chunk: {math.floor(X / 16)}, {math.floor(Z / 16)}")

print(f"Nether Block: {math.floor(X / 8)}, {math.floor(Z / 8)}")
print(f"Nether Chunk: {math.floor((X / 16) / 8)}, {math.floor((Z / 16) / 8)}")