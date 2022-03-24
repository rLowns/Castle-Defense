import pygame
# from main import *

WIDTH  = 1080
HEIGHT = 700

class player_index:

    def __init__(self):

        self.hp = 100 # player's hp
        self.damage = 25 # player's damage
        self.speed = 1 # player's speed
        self.attack_speed = 0.2 # player's attack_speed
        self.color = 'green' # player's color
        self.pos = [200,200] # player's position
        self.size = 30 # player's size
        self.thick_skin = 3 # player's thick of skin
        self.max_hp = 100 # player's max hp
        self.Xchange = 0
        self.Ychange = 0

        # healthbar index
        self.size_cellhealthbar = [250,20]
        self.thick_cellheathbar = 4
        self.pos_thehealthbar = [730,10]
        self.size_healthbar = [250,20]

        # bullet index
        self.pos_bullet = []
        self.size_bullet = 10
        self.speed_bullet = 3
        self.bullets = 0
        self.bullet_target = []

        self.life = True

        self.atbar = 100
        self.max_atbar = 100

        self.screen = pygame.display.get_surface() # get screen

    def draw_player(self):

        pygame.draw.rect(self.screen,self.color ,(self.pos[0],self.pos[1],self.size,self.size))
        pygame.draw.rect(self.screen,'black' ,(self.pos[0],self.pos[1],self.size,self.size),self.thick_skin)

    def draw_healthbar(self):

        pygame.draw.rect(self.screen,'green' ,(self.pos_thehealthbar[0],self.pos_thehealthbar[1],self.size_healthbar[0],self.size_healthbar[1]))
        pygame.draw.rect(self.screen,'brown' ,(self.pos_thehealthbar[0],self.pos_thehealthbar[1],self.size_cellhealthbar[0],self.size_cellhealthbar[1]),self.thick_cellheathbar)


        pygame.draw.rect(self.screen,'orange' ,(730,30,self.atbar,10))
        pygame.draw.rect(self.screen,'brown' ,(730,30,100,10),3)
    def draw_bullet(self):

        for b in range(self.bullets):
            pygame.draw.rect(self.screen, (0,191,255), (self.pos_bullet[b][0],self.pos_bullet[b][1],self.size_bullet,self.size_bullet))

class enemies_index:

    def __init__(self):

        self.pos = [] # enemies's position
        self.size = [] # enemies's size
        self.color = [] #  enemies's color
        self.damage = [] # enemies's damage
        self.speed = [] # enemies's speed
        self.hp = [] # enemies's hp
        self.enemies = 0 # enemies number

        self.time = 0
        self.retime = 750
        self.type_can_append = ['red','blue','black','orange']
        self.all_type = ['red','blue','black']
        self.challenges_to_add_new_type_of_enemy = 15 # need 15 enemies to unlock new enemy'type
        self.now_challenges = 0       

        self.screen = pygame.display.get_surface() # get screen 


    def draw_enemies(self):
        
        for e in range(self.enemies):
            # draw 
            pygame.draw.rect(self.screen, self.color[e], (self.pos[e][0],self.pos[e][1],self.size[e],self.size[e]))

class buff_index:

    def __init__(self):

        self.pos = []
        self.radius = 8
        self.color = [] 
        self.buffs = 0
        self.max_buff = 4
        self.time_life = []

        self.time = 0
        self.retime = 800

        self.max_time_life = 700
        
        self.all_color = ['red','orange','green','blue','black']

        self.Ypos_text = [300,350,400,450]

