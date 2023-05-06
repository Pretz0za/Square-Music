from metronomeextraction import metronomes

boxWidth = 300
squareWidth = 30
distance = boxWidth - squareWidth
frameRate = 30

i=0
for metronome in range(0, len(metronomes), 2):
    if not metronome == len(metronomes)-1:
        if i % 4 == 0:
            print(f'note{int(metronome/2 + 1)} = new Square({distance / (metronomes[metronome][1]*30)}, {distance / (metronomes[metronome+1][1]*30)}, {320 - ((distance / metronomes[metronome][1]) * metronomes[metronome][0])}, {320 - ((distance / metronomes[metronome+1][1]) * metronomes[metronome+1][0])})')
        elif i % 4 == 1:
            print(f'note{int(metronome/2 + 1)} = new Square({-1 * (distance / (metronomes[metronome][1]*30))}, {distance / (metronomes[metronome+1][1]*30)}, {370 - (320 - ((distance / metronomes[metronome][1]) * metronomes[metronome][0]))}, {320 - ((distance / metronomes[metronome+1][1]) * metronomes[metronome+1][0])})')
        elif i % 4 == 2:
            print(f'note{int(metronome/2 + 1)} = new Square({distance / (metronomes[metronome][1]*30)}, {-1 * (distance / (metronomes[metronome+1][1]*30))}, {320 - ((distance / metronomes[metronome][1]) * metronomes[metronome][0])}, {370 - (320 - ((distance / metronomes[metronome+1][1]) * metronomes[metronome+1][0]))})')
        else:
            print(f'note{int(metronome/2 + 1)} = new Square({-1 * (distance / (metronomes[metronome][1]*30))}, {-1 * (distance / (metronomes[metronome+1][1]*30))}, {370 - (320 - ((distance / metronomes[metronome][1]) * metronomes[metronome][0]))}, {370 - (320 - ((distance / metronomes[metronome+1][1]) * metronomes[metronome+1][0]))})')
    else:
        print(f'note{int(metronome/2 + 1)} = new Square({distance / (metronomes[metronome][1]*30)}, {distance / (metronomes[metronome][1]*30)}, {320 - ((distance / metronomes[metronome][1]) * metronomes[metronome][0])}, {320 - ((distance / metronomes[metronome][1]) * metronomes[metronome][0])})')
    i+=1
'''
for metronome in metronomes:
    print(metronome)

i = 1
for metronome in range(len(metronomes)):
    print(f'note{i} = new Square({distance / (metronomes[metronome][1]*30)}, 0, {((distance / metronomes[metronome][1]) * metronomes[metronome][0])}, height/2)')
    i+=1

print(f'note1 = new Square({distance / (metronomes[0][1]*30)}, {distance / (metronomes[3][1]*30)}, {320 - ((distance / metronomes[0][1]) * metronomes[0][0])}, {320 - ((distance / metronomes[3][1]) * metronomes[3][0])})')
print(f'note2 = new Square({distance / (metronomes[1][1]*30)}, {distance / (metronomes[2][1]*30)}, {320 - ((distance / metronomes[1][1]) * metronomes[1][0])}, {320 - ((distance / metronomes[2][1]) * metronomes[2][0])})')
print(f'note3 = new Square({distance / (metronomes[4][1]*30)}, {distance / (metronomes[4][1]*30)}, {320 - ((distance / metronomes[4][1]) * metronomes[4][0])}, {320 - ((distance / metronomes[4][1]) * metronomes[4][0])})')
'''