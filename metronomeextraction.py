from timeinfo import output

times = output

for i in range(len(times)):
    times[i] = round(times[i], 7)
metronomes = []
trash = []



for i in range(len(times)):
    if times[i] in trash:
        continue
    patterns = []
    for j in range(i+1, len(times)):
        if times[j] in trash:
            continue
        if 2*times[j] - times[i] in times:
            counter = 0
            while round(times[i] + (counter * (times[j]-times[i])), 7) in times and not round(times[i] + (counter * (times[j]-times[i])), 7) in trash:
                counter += 1
            patterns.append((times[j]-times[i], counter))

    bestPattern = (0, -1)
    for pattern in patterns:
        if pattern[0] < times[i]:
            continue
        if pattern[1] > bestPattern[1]:
            bestPattern = pattern
    if not (bestPattern[1] == 2 and bestPattern == patterns[0]):
        for j in range(bestPattern[1]):
            trash.append(round(times[i] + (j * bestPattern[0]), 7))
        metronomes.append((times[i], bestPattern[0], bestPattern[1]))

if not len(trash) == len(times):
    for time in times:
        if time in trash:
            continue
        metronomes.append(time, times[-1], 1)
            


# To deal with stand alone notes that aren't a part of any pattern, I should put all "bestPattern"s that have length 2 in a temp list and not append anything from them to trash, and I should come back to them at the end of the code to resolve them.