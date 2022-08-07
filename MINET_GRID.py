import random

steps = 50
time = 0
energy = 3
key = False
launch = 0

actions = ['NEGATIVE_STEPS', 'LOCK', 'SWORDS', 'LAUNCH']

board = {
0:[1,15],
1:[0,2],
2:[1,3],
3:[2,4],
4:[3,5,6],
5:[4,'CIRCUIT'],
6:[4,7],
7:[6,8],
8:[7,9],
9:[8,10],
10:[9,11,14],
11:[10,12],
12:[11,13],
13:[12,'FUEL'],
14:[10,'TOOLS'],
15:[0,16],
16:[15,'FOOD'],
17:[18,'FOOD'],
18:[17,19,20],
19:[18,'ANTENNA'],
20:[18,21],
21:[20,'TOOLS'],
22:[23,'TOOLS'],
23:[22,24],
24:[23,25],
25:[24,26,27,28],
26:[25,'FUEL'],
27:[25,'MEDICATION'],
28:[25,'AUTOMATIC GUNS'],
29:[32,'TOOLS'],
30:[31,'ANTENNA'],
31:[30,32],
32:[29,31,33],
33:[32,34],
34:[33,'AUTOMATIC GUNS'],
35:[36,'AUTOMATIC GUNS'],
36:[35,37],
37:[36,'SOLAR PANEL'],
38:[39,'SOLAR PANEL'],
39:[38,40],
40:[39,'KEY'],
41:[42,'KEY'],
42:[41,43],
43:[42,44],
44:[43,'MANUAL'],
45:[46,'MANUAL'],
46:[45,47],
47:[46,48],
48:[47,49],
49:[48,50,51],
50:[49,'CIRCUIT'],
51:[49,52],
52:[51,53],
53:[52,54],
54:[53,55,56],
55:[54,'FUEL'],
56:[54,'MEDICATION'],
57:[58,'MEDICATION'],
58:[57,59],
59:[58,60,61],
60:[59,'SOLAR_PANEL'],
61:[59,'KEY']}

dotted = {
 9: ['FOOD'],
 'FOOD': [9],
 46: ['SPACE SATELLITE'],
 58: ['SPACE SATELLITE'],
 'SPACE SATELLITE': [46,58],
 'TOOLS': ['AUTOMATIC GUNS'],
 'AUTOMATIC GUNS': ['TOOLS'],
 'FUEL': ['CIRCUIT'],
 'CIRCUIT': ['FUEL'],
}

resources = ['ANTENNA', 'TOOLS', 'CIRCUIT', 'SOLAR PANEL',
             'MANUAL', 'FOOD', 'FUEL', 'AUTOMATIC GUNS',
             'SPACE SATELLITE', 'MEDICATION']

choices = list(range(1,62))
actions = {'NEGATIVE_STEPS':[], 'LOCK':[], 'SWORDS':[], 'LAUNCH':[]}

def choose(n, action):
    for i in range(n):
        x = random.choice(choices)
        actions[action].append(x)
        choices.remove(x)

def main():
    negative_steps = int(input("NEGATIVE STEPS: "))
    lock = int(input("LOCK: "))
    swords = int(input("SWORDS: "))
    launch = int(input("LAUNCH: "))
    choose(negative_steps, 'NEGATIVE_STEPS')
    choose(lock, 'LOCK')
    choose(swords, 'SWORDS')
    choose(launch, 'LAUNCH')
