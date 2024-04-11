import pygame
import sys,math,time

pygame.init()

width,height = 400,700
Screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ping Pong")
bg_color = (255, 251, 240)

class Player():
    def __init__(self,x,y,w,h,col,screen) -> None:
        self.x, self.y = x + screen.get_width()//2 -w//2,y
        self.w , self.h = w,h
        self.col ,self.screen= col,screen
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.is_pressed_right,self.is_pressed_left= False,False
        self.velocity = 5
        
    
    def draw(self):
        pygame.draw.rect(self.screen,self.col,self.rect)
    def update(self):
        if self.is_pressed_right and self.rect.right <= self.screen.get_width():
            self.rect.x += self.velocity 
        elif self.is_pressed_left and self.rect.left >= 0:
            self.rect.x -= self.velocity

        

score_p1 =0
score_p2 =0       



class Ball():
    
    def __init__(self,x,y,w,h,col,screen,player_1,player_2) -> None:
        self.x, self.y = x + screen.get_width()//2 -w//2,y + screen.get_height()//2 -h//2
        self.w , self.h = w,h
        self.col ,self.screen= col,screen
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.b_velocity_x,self.b_velocity_y = 4,4
        self.player_1,self.player_2 = player_1,player_2
        
    def draw(self):
        pygame.draw.ellipse(self.screen,self.col,self.rect)
    def update(self):
        global score_p1,score_p2
        self.rect.x += self.b_velocity_x
        self.rect.y += self.b_velocity_y

        if self.rect.left >= self.screen.get_width() or self.rect.left <= 0 :
            self.b_velocity_x *= -1 
        elif self.rect.bottom >= self.screen.get_height() :
            self.rect.x = self.x
            self.rect.y = self.y
            time.sleep(0.1)
            score_p1 +=1
        elif self.rect.top <= 0 :
            self.rect.x = self.x
            self.rect.y = self.y
            time.sleep(0.1)
            score_p2 +=1
           
        # collision with the ball
        if self.rect.colliderect(self.player_1) or self.rect.colliderect(self.player_2):
            self.b_velocity_y *= -1
            

                
           


            


         
        

def run_game():
    clock = pygame.time.Clock()
    running = True
    p_col = (56, 55, 52)
    b_col = (112, 112, 112)
    FPS = 60
    player_1 = Player(0,0,100,15,p_col,Screen)
    player_2 = Player(0,height-15,100,15,p_col,Screen)
    
    
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    
    ball = Ball(0,0,16,16,b_col,Screen,player_1,player_2)
    
    while running:
        clock.tick(FPS)
        score_txt_p1 =font.render(str(score_p1), True, p_col)
        textRect_p1 = score_txt_p1.get_rect()
        textRect_p1.center = (width // 2, height // 2 - 15)
        score_txt_p2 =font.render(str(score_p2), True, p_col)
        textRect_p2 = score_txt_p2.get_rect()
        textRect_p2.center = (width // 2 , height // 2+ 20)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player_1.is_pressed_right = True
                elif event.key == pygame.K_LEFT:
                    player_1.is_pressed_left = True
                elif event.key == pygame.K_d:
                    player_2.is_pressed_right = True
                elif event.key == pygame.K_a:
                    player_2.is_pressed_left = True
            elif event.type ==pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player_1.is_pressed_right = False
                elif event.key == pygame.K_LEFT:
                    player_1.is_pressed_left = False
                elif event.key == pygame.K_d:
                    player_2.is_pressed_right = False
                elif event.key == pygame.K_a:
                    player_2.is_pressed_left = False

            # player 2 controlls
            
                
        

       


        Screen.fill(bg_color)
        Screen.blit(score_txt_p1, textRect_p1)
        Screen.blit(score_txt_p2, textRect_p2)
        pygame.draw.aaline(Screen,p_col,(0,height/2),(width,height/2))
        player_1.draw()
        player_2.draw()
        ball.draw()
       
        player_1.update()
        player_2.update()
        ball.update()
        print(score_p1,score_p2)
        
        pygame.display.update()
run_game()
