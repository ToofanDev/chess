from tkinter import PhotoImage
from turtle import *
import random

root = Screen()
root.setup(width=1100,height=625)
root.bgpic('MINET_IMAGE.png')

root.addshape('LAUNCH', Shape("image", PhotoImage(file="LAUNCH.gif").subsample(3, 3)))
root.addshape('NEGATIVE_STEPS', Shape("image", PhotoImage(file="NEGATIVE_STEPS.gif").subsample(3, 3)))
root.addshape('LOCK', Shape("image", PhotoImage(file="LOCK.gif").subsample(3, 3)))
root.addshape('SWORDS', Shape("image", PhotoImage(file="SWORDS.gif").subsample(3, 3)))
root.addshape('KEY', Shape("image", PhotoImage(file="KEY.gif").subsample(4,3)))

coords = {
1:(-287.0,-193.0),
2:(-243.0,-192.0),
3:(-200.0,-193.0),
4:(-200.0,-150.0),
5:(-157.0,-149.0),
6:(-199.0,-108.0),
7:(-243.0,-107.0),
8:(-286.0,-106.0),
9:(-287.0,-64.0),
10:(-288.0,-20.0),
11:(-244.0,-22.0),
12:(-199.0,-20.0),
13:(-157.0,-19.0),
14:(-287.0,22.0),
15:(-435.0,-130.0),
16:(-437.0,-85.0),
17:(-436.0,44.0),
18:(-436.0,86.0),
19:(-436.0,129.0),
20:(-393.0,86.0),
21:(-350.0,86.0),
22:(-223.0,86.0),
23:(-180.0,86.0),
24:(-136.0,86.0),
25:(-92.0,86.0),
26:(-94.0,43.0),
27:(-49.0,86.0),
28:(-94.0,130.0),
29:(-287.0,150.0),
30:(-372.0,194.0),
31:(-328.0,192.0),
32:(-287.0,192.0),
33:(-243.0,192.0),
34:(-200.0,192.0),
35:(15.0,192.0),
36:(60.0,192.0),
37:(101.0,192.0),
38:(229.0,192.0),
39:(272.0,193.0),
40:(272.0,150.0),
41:(250.0,1.0),
42:(250.0,-43.0),
43:(251.0,-85.0),
44:(252.0,-129.0),
45:(188.0,-192.0),
46:(144.0,-193.0),
47:(102.0,-192.0),
48:(58.0,-192.0),
49:(15.0,-192.0),
50:(-28.0,-191.0),
51:(15.0,-150.0),
52:(15.0,-107.0),
53:(15.0,-63.0),
54:(15.0,-20.0),
55:(-27.0,-21.0),
56:(14.0,23.0),
57:(79.0,86.0),
58:(122.0,86.0),
59:(165.0,86.0),
60:(164.0,129.0),
61:(208.0,86.0),
0: (-395.0,-185.0),
'CIRCUIT': (-91.0,-163.0),
'MANUAL': (251.0,-182.0),
'FOOD': (-435.0,-22.0),
'FUEL': (-99.0,-15.0),
'SPACE SATELLITE': (126.0,-33.0),
'TOOLS': (-289.0,92.0),
'MEDICATION': (13.0,102.0),
'KEY': (267.0,96.0),
'ANTENNA': (-436.0,198.0),
'AUTOMATIC GUNS': (-99.0,195.0),
'SOLAR PANEL': (162.0,206.0)}

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
60:[59,'SOLAR PANEL'],
61:[59,'KEY'],
'ANTENNA':[19,30],
'AUTOMATIC GUNS':[28,34,35],
'SOLAR PANEL':[37,38,60],
'TOOLS':[14,21,22,29],
'MEDICATION':[27,56,57],
'KEY':[40,41,61],
'FOOD':[16,17],
'FUEL':[13,26,55],
'SPACE SATELLITE':[],
'CIRCUIT':[5,50],
'MANUAL':[44,45]
}

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

def resources_collected(arr):
    for resource in resources:
        if resource not in arr:
            return False
    return True

def get_path(negative_steps, locks, swords, launches):
    if launches>=5 and locks<=5 and negative_steps<=5 and swords<=5: return 3
    if launches>=1 and locks<=10 and negative_steps<=10 and swords<=10: return 4
    res = []
    for i in range(70):
        temp = []
        return False
        for path in res:
            if path[0]==0: continue
            for j in board[path[5][-1]]:
                if j!=path[4] or type(path[5][-1])==str:
                    if j in actions['NEGATIVE_STEPS']:
                        if path[0]-5>0:
                            temp.append([path[0]-6,path[1],path[2],path[3],path[5][-1],path[5]+[j]])
                    elif j in actions['LOCK']:
                        if path[3]:
                            temp.append([path[0]-1,path[1],path[2],path[3],path[5][-1],path[5]+[j]])
                    elif j in actions['SWORDS']:
                        if (path[1]>1 or i%16==15 or resources_collected(path[5]+[j])):
                            temp.append([path[0]-1,path[1]-1,path[2],path[3],path[5][-1],path[5]+[j]])
                    elif j in actions['LAUNCH']:
                        temp.append([path[0]-1,path[1],path[2]+1,path[3],path[5][-1],path[5]+[j]])
                    elif j=='KEY':
                        temp.append([path[0]-1,path[1],path[2],True,path[5][-1],path[5]+[j]])
                    else:
                        temp.append([path[0]-1,path[1],path[2],path[3],path[5][-1],path[5]+[j]])
                    if resources_collected(temp[-1][5]):
                        print(temp[-1][5])
            if path[5][-1] in dotted and path[2]>0:
                for dot in dotted[path[5][-1]]:
                    temp.append([path[0]-1,path[1],path[2]-1,path[3],path[5][-1],path[5]+[dot]])
                    if resources_collected(temp[-1][5]):
                        print(temp[-1][5])
        res = temp

def choose(n, action):
    actions[action] = []
    for i in range(n):
        x = random.choice(choices)
        actions[action].append(x)
        choices.remove(x)
        t = Turtle(action)
        t.speed(0)
        t.up()
        t.setpos(coords[x])
        action_turtles[x] = t

def move(path):
    mover.showturtle()
    mover.setpos(*coords[path])
    moves.append(path)

def setup(days=False):
    root.tracer(0)
    fixed_writer.clear()
    fixed_writer.setpos(375,-150)
    fixed_writer.pencolor('#C4C4C4')
    fixed_writer.write("Arrow Keys to MOVE\n\nW,A,S,D to LAUNCH\n\nEscape to RESTART", font=('Arial', 12, 'bold'))
    fixed_writer.setpos(375,-200)
    fixed_writer.pencolor('#73FFE7')
    fixed_writer.write("OPTIMAL SOLUTION", font=('Arial', 12, 'bold', 'underline'))
    fixed_writer.setpos(375,-230)
    if days==False:
        fixed_writer.pencolor('#FF3131')
        fixed_writer.write("NOT POSSIBLE", font=('Arial', 16, 'bold'))
    else:
        fixed_writer.pencolor('light green')
        fixed_writer.write(f"{days} DAYS", font=('Arial', 16, 'bold'))
    root.tracer(1)

def stats(steps, hours, energy, launch, keys):    
    root.tracer(0)
    writer.clear()
    #DAY
    writer.setpos(-75,265)
    writer.pencolor('light blue')
    writer.write(f"DAY {int(hours/8)+1}", font = ('Arial',20,'bold'), align='center')
    #BOX
    writer.pencolor('white')
    writer.fillcolor('black')
    writer.setpos(375,223)
    writer.begin_fill()
    for i in range(2):
        writer.fd(100)
        writer.lt(90)
        writer.fd(25)
        writer.lt(90)
    writer.end_fill()
    writer.setpos(378,225)
    writer.write("Steps Left", font=('Arial', 12, 'bold'))

    writer.setpos(375,174)
    writer.begin_fill()
    for i in range(2):
        writer.fd(100)
        writer.lt(90)
        writer.fd(25)
        writer.lt(90)
    writer.end_fill()
    writer.setpos(378,176)
    writer.write("Hours Spent", font=('Arial', 12, 'bold'))

    writer.setpos(375,125)
    writer.begin_fill()
    for i in range(2):
        writer.fd(100)
        writer.lt(90)
        writer.fd(25)
        writer.lt(90)
    writer.end_fill()
    writer.setpos(378,127)
    writer.write("Launch", font=('Arial', 12, 'bold'))

    writer.setpos(375,76)
    writer.begin_fill()
    for i in range(2):
        writer.fd(100)
        writer.lt(90)
        writer.fd(25)
        writer.lt(90)
    writer.end_fill()
    writer.setpos(378,78)
    writer.write("Energy", font=('Arial', 12, 'bold'))

    writer.pencolor('blue')
    writer.fillcolor('white')
    #STEPS LEFT
    writer.setpos(484,223)
    writer.begin_fill()
    for i in range(4):
        writer.fd(25)
        writer.lt(90)
    writer.end_fill()
    writer.setpos(499,220)
    writer.write(steps, font=('Arial', 20, 'bold'), align='center')
    #HOURS SPENT
    writer.setpos(484,174)
    writer.begin_fill()
    for i in range(4):
        writer.fd(25)
        writer.lt(90)
    writer.end_fill()
    writer.setpos(498,178)
    writer.write(hours, font=('Arial', 12, 'bold'), align='center')
    #LAUNCH
    writer.setpos(484,125)
    writer.begin_fill()
    for i in range(4):
        writer.fd(25)
        writer.lt(90)
    writer.end_fill()
    writer.setpos(499,122)
    writer.write(launch, font=('Arial', 20, 'bold'), align='center')
    #ENERGY
    writer.setpos(484,76)
    writer.begin_fill()
    for i in range(4):
        writer.fd(25)
        writer.lt(90)
    writer.end_fill()
    writer.setpos(499,73)
    writer.write(energy, font=('Arial', 20, 'bold'), align='center')
    #KEY
    if keys:
        key.showturtle()
    else:
        key.hideturtle()

    root.tracer(1)

choices = list(range(1,62))
actions = {}

mover = Turtle('circle', visible=False)
mover.color('green')
mover.pensize(3)

key = Turtle('KEY', visible=False)
key.up()
key.setpos(450,10)

writer = Turtle(visible=False)
writer.up()
fixed_writer = Turtle(visible=False)
fixed_writer.up()

def gameover():
    if resources_collected(moves):
        text = root.textinput("GAME OVER!","GAME WON: Visited all resource blocks!\n                         Do you want to play again?                         ")
        if text==None or (text!='' and text.lower()[0]=='n'):
            root.bye()
            return
        main()

    elif (not up(False) and not right(False) and not left(False) and not down(False)
    and not W(False) and not A(False) and not S(False) and not D(False)):
        text = root.textinput("GAME OVER!","GAME LOST: No possible move!\n                         Do you want to play again?                         ")
        if text==None or (text!='' and text.lower()[0]=='n'):
            root.bye()
            return
        main()
    elif stat[1]%8==0:
        if current in resources or current==0:
            stat[0]+=5
            stat[2]=3
            stats(*stat)
        else:
            text = root.textinput("GAME OVER!","GAME LOST: Not at a resource block!\n                         Do you want to play again?                         ")
            if text==None or (text!='' and text.lower()[0]=='n'):
                root.bye()
                return
            main()

def check(x, update=True, launch=False):
    global current
    if stat[0]>0 and stat[2]>0:
        if launch:
            if stat[3]>0:
                if not update:
                    return True
                move(x)
                stat[0]-=1
                stat[1]+=0.5
                stat[3]-=1
                stats(*stat)
                current = x
        elif x in actions['NEGATIVE_STEPS']:
            if stat[0]>5:
                if not update:
                    return True
                move(x)
                stat[0]-=6
                stat[1]+=0.5
                stats(*stat)
                current = x
                actions['NEGATIVE_STEPS'].remove(x)
                action_turtles[x].hideturtle()
        elif x in actions['LOCK']:
            if stat[4]:
                if not update:
                    return True
                move(x)
                stat[0]-=1
                stat[1]+=0.5
                stats(*stat)
                current = x
                actions['LOCK'].remove(x)
                action_turtles[x].hideturtle()
        elif x in actions['SWORDS']:
            if stat[2]>0:
                if not update:
                    return True
                move(x)
                stat[0]-=1
                stat[1]+=0.5
                stat[2]-=1
                stats(*stat)
                current = x
                actions['SWORDS'].remove(x)
                action_turtles[x].hideturtle()
        elif x in actions['LAUNCH']:
            if not update:
                return True
            move(x)
            stat[3]+=1
            stat[0]-=1
            stat[1]+=0.5
            stats(*stat)
            current = x
            actions['LAUNCH'].remove(x)
            action_turtles[x].hideturtle()
        elif x=='KEY':
            if not update:
                return True
            move(x)
            stat[4]=True
            stat[0]-=1
            stat[1]+=0.5
            stats(*stat)
            current = x
        else:
            if not update:
                return True
            move(x)
            stat[0]-=1
            stat[1]+=0.5
            stats(*stat)
            current = x

def up(update=True):
    global current, moving
    res = False
    if not moving:
        moving = True
        c = coords[current][1]
        for x in board[current]:
            if coords[x][1]-c > 20:
                res = check(x,update)
                break
        moving = False
        if update: gameover()
        return res
def down(update=True):
    global current, moving
    res = False
    if not moving:
        moving = True
        c = coords[current][1]
        for x in board[current]:
            if c-coords[x][1] > 20:
                res = check(x,update)
                break
        moving = False
        if update: gameover()
        return res
def right(update=True):
    global current, moving
    res = False
    if not moving:
        moving = True
        c = coords[current][0]
        for x in board[current]:
            if coords[x][0]-c > 20:
                res = check(x,update)
                break
        moving = False
        if update: gameover()
        return res
def left(update=True):
    global current, moving
    res = False
    if not moving:
        moving = True
        c = coords[current][0]
        for x in board[current]:
            if c-coords[x][0] > 20:
                res = check(x,update)
                break
        moving = False
        if update: gameover()
        return res

def W(update=True):
    global current, moving
    res = False
    if not moving:
        moving = True
        c = coords[current][1]
        if current in dotted:
            for x in dotted[current]:
                if coords[x][1]-c > 20:
                    res = check(x,update,True)
                    break
            moving = False
            if update: gameover()
            return res
def A(update=True):
    global current, moving
    res = False
    if not moving:
        moving = True
        c = coords[current][0]
        if current in dotted:
            for x in dotted[current]:
                if c-coords[x][0] > 20:
                    res = check(x,update,True)
                    break
            moving = False
            if update: gameover()
            return res
def S(update=True):
    global current, moving
    res = False
    if not moving:
        moving = True
        c = coords[current][1]
        if current in dotted:
            for x in dotted[current]:
                if c-coords[x][1] > 20:
                    res = check(x,update,True)
                    break
            moving = False
            if update: gameover()
            return res
def D(update=True):
    global current, moving
    res = False
    if not moving:
        moving = True
        c = coords[current][0]
        if current in dotted:
            for x in dotted[current]:
                if coords[x][0]-c > 20:
                    res = check(x,update,True)
                    break
            moving = False
            if update: gameover()
            return res

current = 0
moving = False
stat = [50,0.0,3,0,False]
action_turtles = {}
moves = []
def main():
    global stat, current, moving, action_turtles, moves
    mover.hideturtle()
    mover.clear()
    mover.up()
    mover.setpos(-395,-185)
    mover.down()
    key.hideturtle()
    writer.clear()
    for t in action_turtles: action_turtles[t].hideturtle()
    
    action_turtles = {}
    negative_steps = int(root.numinput("Game Setup", "                         NEGATIVE STEPS                         ", default=0, minval=0, maxval=15))
    locks = int(root.numinput("Game Setup", "                              LOCKS                              ", default=0, minval=0, maxval=15))
    swords = int(root.numinput("Game Setup", "                              SWORDS                              ", default=0, minval=0, maxval=15))
    launches = int(root.numinput("Game Setup", "                         LAUNCHES                         ", default=0, minval=0, maxval=15))
    choose(negative_steps, 'NEGATIVE_STEPS')
    choose(locks, 'LOCK')
    choose(swords, 'SWORDS')
    choose(launches, 'LAUNCH')

    setup(get_path(negative_steps, locks, swords, launches))
    mover.showturtle()
    current = 0
    moves = []
    moving = False
    stat = [50,0,3,0,False]
    stats(*stat)
    root.listen()
    root.onkey(up, "Up")
    root.onkey(down, "Down")
    root.onkey(left, "Left")
    root.onkey(right, "Right")
    root.onkey(main, "Escape")
    root.onkey(W, "w")
    root.onkey(A, "a")
    root.onkey(S, "s")
    root.onkey(D, "d")

main()
root.mainloop()
