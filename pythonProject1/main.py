import itertools

x = list(itertools.product((2, 4, 6, 10), repeat = 3))
probs = [0, 0, .3, 0, .35, 0, .25, 0, 0, 0, .1]
i = 1
means = [0, 2, 4, 6, 8]
sampleDistribution = [0, 0, 0, 0, 0]
variance = 0
expectedValue = 0

txt1 = ", Mean: {textMean:.2f}"
txt2 = ", Probability: {textProb:.6f}"
txt3 = ", Max: {textMax:.1f}"
txt4 = ", Min: {textMin:.1f}"
txt5 = ", Range: {textRange:.1f}"

for y in x:
    mean = (y[0] + y[1] + y[2]) / 3
    probability = probs[y[0]] * probs[y[2]] * probs[y[2]]
    print(str(i) + ") " + str(y) + txt1.format(textMean = mean) + txt2.format(textProb = probability) + txt3.format(textMax = max(y[0], y[1], y[2])) + txt4.format(textMin = min(y[0], y[1], y[2])) + txt5.format(textRange = max(y[0], y[1], y[2]) - min(y[0], y[1], y[2])))
    i = i + 1
    sampleDistribution[means.index(max(y[0], y[1], y[2]) - min(y[0], y[1], y[2]))] += probability

i = 0
while i < 5:
    expectedValue += means[i] * sampleDistribution[i]
    i = i + 1

i = 0
while i < 5:
    variance += pow((means[i] - expectedValue), 2) * sampleDistribution[i]
    i = i + 1

print(means)
print(sampleDistribution)

print(expectedValue)
print(variance)