import pygame, sys, random
from index import *

# setup 
pygame.init()

# set screen
Screen = pygame.display.set_mode((WIDTH,HEIGHT))

# set caption
pygame.display.set_caption("Castle Defense")

# set run fps
clock = pygame.time.Clock()

# get index
Player = player_index()
Enemies = enemies_index()
Buffs = buff_index()

Enemy = {
    'red':{
        'damage':0.2,
        'speed':1,
        'size':40,
        'hp':90
    },
    'blue':{
        'damage':0.6,
        'speed':0.5,
        'size':90,
        'hp':190
    },
    'black':{
        'damage':0.05,
        'speed':3,
        'size':25,
        'hp':90
    },
    'orange':{
        'damage':1,
        'speed':5,
        'size':15,
        'hp':1
    }
}

# define
def create_new_enemy(color):
    global Enemies

    Enemies.hp.append(Enemy[color]['hp'])
    Enemies.damage.append(Enemy[color]['damage'])
    Enemies.speed.append(Enemy[color]['speed'])
    Enemies.size.append(Enemy[color]['size'])
    From = random.choice(['on','under','left','right'])
    ListFrom = {
        'on':{
            'x':[0,sidesize[0]],
            'y':[-100,-10]
        },
        'under':{
            'x':[0,sidesize[0]],
            'y':[sidesize[1],sidesize[1]+10]
        },
        'left':{
            'x':[-100,-10],
            'y':[0,sidesize[1]]
        },
        'right':{
            'x':[sidesize[0],sidesize[0]+100],
            'y':[0,sidesize[1]]
        }
    }
    Enemies.pos.append([random.randint(ListFrom[From]['x'][0],ListFrom[From]['x'][1]),random.randint(ListFrom[From]['y'][0],ListFrom[From]['y'][1])])
    Enemies.enemies+=1

def Collision(Apos,Bpos,Asize,Bsize):

    if Apos[0]<=Bpos[0]+Bsize and Bpos[0] <= Apos[0]+Asize   and Apos[1]<=Bpos[1]+Bsize and Bpos[1] <= Apos[1]+Asize:
        return True
    else:
        return False

# def InObject(Apos,Ipos,Asize):
    
#     if Ipos[0] >= Apos[0] and Ipos[0] <= Apos[0]+Asize and Ipos[1] >= Apos[1] and Ipos[1] <= Apos[1]+Asize:
#         return True
#     else:
#         return False

def message(msg,pos,size,color):
    font = pygame.font.Font(None, size)
    text = font.render(msg, True, color)
    Screen.blit(text, (pos[0], pos[1]))

def Button(msg,color_msg,base_color,change_color,size_button,pos_button):

    

    if MousePos[0]>=pos_button[0] and MousePos[0] <= pos_button[0]+size_button[0] and MousePos[1]>=pos_button[1] and MousePos[1] <= pos_button[1]+size_button[1]:
        color_button = change_color
        
    else:
        color_button = base_color
    pygame.draw.rect(Screen, color_button, (pos_button[0],pos_button[1],size_button[0],size_button[1]))
    font = pygame.font.Font(None, int(size_button[0]/(len(msg)*0.5)))
    text = font.render(msg, True, color_msg)
    Screen.blit(text, (pos_button[0]+len(msg)*2,pos_button[1]+len(msg)*2))

def ClickButton(Apos,Asize):

    if MousePos[0]>=Apos[0] and MousePos[0] <= Apos[0]+Asize[0] and MousePos[1]>=Apos[1] and MousePos[1] <= Apos[1]+Asize[1]:
        return True
    else:
        return False
    
def BulletHandle():
    Reset = False
    global Player
    global Enemies

    for b in range(Player.bullets):
        
        if Player.bullet_target[b][0] >= Player.pos_bullet[b][0] and Player.pos_bullet[b][0]+Player.size_bullet<sidepos[0]+sidesize[0]:
            Player.pos_bullet[b][0]+=Player.speed_bullet
        if Player.bullet_target[b][0] <= Player.pos_bullet[b][0] and Player.pos_bullet[b][0]>sidepos[0]:
            Player.pos_bullet[b][0]-=Player.speed_bullet   

        if Player.bullet_target[b][1] >= Player.pos_bullet[b][1] and Player.pos_bullet[b][1]+Player.size_bullet<sidepos[1]+sidesize[1]:
            Player.pos_bullet[b][1]+=Player.speed_bullet
        if Player.bullet_target[b][1] <= Player.pos_bullet[b][1] and Player.pos_bullet[b][1]>sidepos[1]:
            Player.pos_bullet[b][1]-=Player.speed_bullet 

        for e in range(Enemies.enemies):
            if Collision(Player.pos_bullet[b],Enemies.pos[e],Player.size_bullet,Enemies.size[e]):
                Enemies.hp[e] -= Player.damage
                Player.bullets-=1
                del Player.bullet_target[b]
                del Player.pos_bullet[b]
                Reset = True
                if Enemies.hp[e] <=0:
                    if Enemies.color[e] == 'red':
                        Player.damage+=1
                    if Enemies.color[e] == 'blue':
                        Player.hp += 5
                        t = 5/Player.hp
                        Player.size_healthbar[0] += t * Player.size_cellhealthbar[0]
                        if Player.hp > Player.max_hp:
                            Player.hp = Player.max_hp
                            Player.size_healthbar[0] = Player.size_cellhealthbar[0]
                    if Enemies.color[e] == 'black':
                        Buffs.retime -= Buffs.retime * 0.005
                    if Enemies.color[e] == 'orange':
                        Player.attack_speed += 0.01


                    del Enemies.pos[e]
                    del Enemies.speed[e]
                    del Enemies.damage[e]
                    del Enemies.color[e]
                    del Enemies.size[e]
                    del Enemies.hp[e]
                    Enemies.enemies-=1     
                break
        if Reset==True:
            Reset = False
            break
            # if InObject(Player.pos_bullet[b], Player.bullet_target[b], Player.size_bullet):
            #     Player.bullets-=1
            #     del Player.bullet_target[b]
            #     del Player.pos_bullet[b]
            #     print("AAAAAA")
            #     break

def EnemiesHandle():
    global Player
    global Enemies

    for e in range(Enemies.enemies):
        if Player.pos[0] > Enemies.pos[e][0]:
            Enemies.pos[e][0] += Enemies.speed[e]
        if Player.pos[0] < Enemies.pos[e][0]:
            Enemies.pos[e][0] -= Enemies.speed[e]
    
        if Player.pos[1] > Enemies.pos[e][1]:
            Enemies.pos[e][1] += Enemies.speed[e]
        if Player.pos[1] < Enemies.pos[e][1]:
            Enemies.pos[e][1] -= Enemies.speed[e]

        if Collision(Player.pos, Enemies.pos[e], Player.size, Enemies.size[e]):

            Player.hp -= Enemies.damage[e]
            t = Enemies.damage[e]/Player.max_hp
            Player.size_healthbar[0] -= t * Player.size_cellhealthbar[0]

            if Player.hp <= 0 :
                Player.life = False

def create_new_buff(color):
    
    global Buffs
    
    Buffs.pos.append([random.randint(5, sidepos[0]+sidesize[0]),random.randint(5, sidepos[1]+sidesize[1])])
    Buffs.buffs+=1
    Buffs.time_life.append(0)

def BuffHandle():

    global Player
    global Buffs

    for bu in range(Buffs.buffs):
        
        Buffs.time_life[bu]+=1

        pygame.draw.circle(Screen, Buffs.color[bu], (Buffs.pos[bu][0],Buffs.pos[bu][1]), Buffs.radius)


        if Buffs.pos[bu][0] >=  Player.pos[0] and Buffs.pos[bu][0] <= Player.pos[0]+Player.size and Buffs.pos[bu][1] >=  Player.pos[1] and Buffs.pos[bu][1] <= Player.pos[1]+Player.size:
            

            if Buffs.color[bu] == 'red':
                Player.damage += 5
            if Buffs.color[bu] == 'green' :
                Player.hp+=15
                t = 15/Player.max_hp
                Player.size_healthbar[0] += t*Player.size_cellhealthbar[0]
                if Player.hp > Player.max_hp:
                    Player.hp = Player.max_hp
                    Player.size_healthbar[0] = Player.size_cellhealthbar[0]
            if Buffs.color[bu] == 'blue':
                Player.speed+=0.1
            if Buffs.color[bu] == 'orange':
                Player.attack_speed+=0.1
            if Buffs.color[bu] == 'black':
                Buffs.retime -= Buffs.retime*0.05
                

            del Buffs.time_life[bu]
            del Buffs.pos[bu]
            del Buffs.color[bu]
            Buffs.buffs -= 1
            
            break
            

        if Buffs.time_life[bu] >= Buffs.max_time_life:

            del Buffs.time_life[bu]
            del Buffs.pos[bu]
            del Buffs.color[bu]
            Buffs.buffs -= 1

            break

    message("Green dot         : healing 15 HP", [730,200+50], 20, 'green')
    message("Kill green enemy  : healing 5 HP", [730,230+50], 20, "green")
    message("Red dot           : + 5 damage", [730,270+50], 20, 'red')
    message("Kill red enemy    : + 1 damage", [730,300+50], 20, "red")
    message("Orange dot        : + 0.05 spawn speed", [730,330+50], 20, 'orange')
    message("Kill Orange enemy : + 0.01 spawn speed", [730,360+50], 20, 'orange')
    message("Blue dot          : + 0.1 speed", [730,390+50], 20, 'blue')
    message("Black dot         : spawn buff's cooldown -5%", [730,420+50],20 , 'black')
    message("Kill black enemy  : spawn buff's cooldown -0.5%", [730,450+50], 20, "black")
    
sidepos = [10,10]
sidesize = [700,500]
w = ""
# main gameloop
while True:

    MousePos = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        # close pygame
        if ev.type == pygame.QUIT:    
            pygame.quit()
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_w :
                w = 'up'
            elif ev.key == pygame.K_s:
                w = 'down'
            elif ev.key == pygame.K_d :
                w = "right"
            elif ev.key == pygame.K_a:
                w = "left"
            else:
                w = ""
        if ev.type == pygame.MOUSEBUTTONDOWN and Player.atbar >= int(Player.max_atbar/2):#Collision(Player.pos,Enemies.pos[e],Player.size,Enemies.size[e])
            Player.bullets +=1
            Player.pos_bullet.append([Player.pos[0]+Player.size_bullet,Player.pos[1]+Player.size_bullet])
            Player.bullet_target.append(MousePos)
            Player.atbar -= int(Player.max_atbar/2)
        if ev.type == pygame.MOUSEBUTTONDOWN and ClickButton([WIDTH/2-100,HEIGHT/2],[200,50]) and Player.life == False :
            Player.life = True
            Player = player_index()
            Enemies = enemies_index()
            Buffs = buff_index()
        
    
    if Player.life:
        BulletHandle()
        EnemiesHandle()
        BuffHandle()

        Player.draw_player()
        Player.draw_healthbar()
        Player.draw_bullet()

    
        if w == 'up' and Player.pos[1]>sidepos[1]>0:
            Player.pos[1]-=Player.speed
        if w == 'down' and Player.pos[1]+Player.size<sidepos[1]+sidesize[1]:
            Player.pos[1]+=Player.speed
        if w == 'right' and Player.pos[0]+Player.size<sidepos[0]+sidesize[0]:
            Player.pos[0]+=Player.speed
        if w == 'left' and Player.pos[0]>sidepos[0]:
            Player.pos[0]-=Player.speed
        Enemies.draw_enemies()

        Enemies.time +=1
        if Enemies.time >= Enemies.retime : 
            if Enemies.retime > 400:
                Enemies.retime-=1
            Enemies.time = 0
            COLOR = random.choice(Enemies.type_can_append)
            Enemies.color.append(COLOR)
            create_new_enemy(COLOR)
        
        Buffs.time +=1
        if Buffs.time >= Buffs.retime :
            Buffs.time = 0
            if Buffs.buffs <= Buffs.max_buff:
                COLOR = random.choice(Buffs.all_color)
                Buffs.color.append(COLOR)
                create_new_buff(COLOR)

        pygame.draw.rect(Screen, 'red', (sidepos[0],sidepos[1],sidesize[0],sidesize[1]),5)

        message(f"Damage: {int(Player.damage)}", [730,50], 35, "black")
        message(f"Speed: {int(Player.speed)}", [730,100], 35, "black")
        message(f"Spawn: {int(Player.attack_speed)}", [730,150], 35, "black")
        message(f"{int(Player.hp)}/{int(Player.max_hp)}", [820,13], 25,"black")

        if Player.atbar < Player.max_atbar:
            Player.atbar += (Player.attack_speed/Player.max_atbar) * Player.max_atbar

    else:
        message("You lose!", [WIDTH/2-45,HEIGHT/2-45], 45, "red")
        Button("Play again", 'black', 'red', 'green', [200,50], [WIDTH/2-50,HEIGHT/2])
    
    
    # display
    pygame.display.update()
    Screen.fill('white')

    clock.tick(60)
