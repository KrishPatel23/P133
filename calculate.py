import csv
from collections import Counter

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
Weights = []

for i in range(len(data)):
    weight = data[i][2]
    Weights.append(float(weight))

Weights.sort()
n = len(Weights)
totalWeight = 0

for x in Weights:
    totalWeight += x


mean = totalWeight/n
print('The Mean Weight of the data is: '+str(mean))


if n%2 == 0:
    m1 = float(Weights[n//2])
    m2 = float(Weights[n//2 - 1])
    median = (m1+m2)/2
else:
    median = Weights[n//2]

print("The Median Weight of the data is: "+str(median))


mode_data = Counter(Weights)

mode_data_for_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    '105-115':0,
    '115-125':0,
    '125-135':0,
    '135-145':0,
    '145-155':0,
    '155-165':0,
    '165-175':0
    }

for weight,occurance in mode_data.items():
    if 75<float(weight)<85:
        mode_data_for_range["75-85"] += occurance
    elif 85<float(weight)<95:
        mode_data_for_range["85-95"] += occurance
    elif 95<float(weight)<105:
        mode_data_for_range["95-105"] += occurance
    elif 105<float(weight)<115:
        mode_data_for_range["105-115"] += occurance
    elif 115<float(weight)<125:
        mode_data_for_range["115-125"] += occurance
    elif 125<float(weight)<135:
        mode_data_for_range["125-135"] += occurance
    elif 135<float(weight)<145:
        mode_data_for_range["135-145"] += occurance
    elif 145<float(weight)<155:
        mode_data_for_range["145-155"] += occurance
    elif 155<float(weight)<165:
        mode_data_for_range["155-165"] += occurance
    elif 165<float(weight)<175:
        mode_data_for_range["165-175"] += occurance

mode_range,mode_occurance = 0,0
for range,occurance in mode_data_for_range.items():
    if occurance>mode_occurance:
        mode_range,mode_occurance = [int(range.split("-")[0]),int(range.split("-")[1])],occurance

mode = float(mode_range[0]+mode_range[1])/2
print(f"The Mode of the data is {mode:2f}")
