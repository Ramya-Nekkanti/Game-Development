import pygame

pygame.init()
pygame.font.init()

WIDTH, HEIGHT= 900, 500
WIN = pygame.display.set_mode([WIDTH, HEIGHT])
#To change the caption of the window
pygame.display.set_caption("My First Pygame!")
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BORDER = pygame.Rect(WIDTH//2 - 5,0,10,HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound("Gun+Silencer.mp3")
BULLET_FIRE_SOUND = pygame.mixer.Sound("Gun+Fire.mp3")

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
FPS = 60
VEL = 5
BULL_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH , SPACESHIP_HEIGHT=55,40

GREEN_HIT = pygame.USEREVENT + 1
RED_HIT= pygame.USEREVENT + 2

GREEN_SPACESHIP_IMAGE = pygame.image.load('Green_Spaceship.png')
GREEN_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(GREEN_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
RED_SPACESHIP_IMAGE = pygame.image.load('Red_Spaceship.png')
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

SPACE = pygame.transform.scale(pygame.image.load('Background.png'), (WIDTH, HEIGHT))

def draw_window(green,red,green_bullets, red_bullets, green_health, red_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    green_health_text= HEALTH_FONT.render("Health: " + str(green_health), 1 , WHITE)
    red_health_text= HEALTH_FONT.render("Health: " + str(red_health), 1 , WHITE)
    WIN.blit(green_health_text, (WIDTH - green_health_text.get_width() -10, 10))
    WIN.blit(red_health_text, (10, 10))
    WIN.blit(GREEN_SPACESHIP,(green.x,green.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    
    for bullet in green_bullets:
        pygame.draw.rect(WIN,GREEN, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.display.update()

def green_handle_movement(keys_pressed, green):
    if keys_pressed[pygame.K_a] and green.x - VEL > 0: #Left
        green.x -= VEL
    if keys_pressed[pygame.K_d] and green.x + VEL + green.width < BORDER.x: #Right
        green.x += VEL
    if keys_pressed[pygame.K_w] and green.y - VEL > 0: #top
        green.y -= VEL
    if keys_pressed[pygame.K_s]and green.y + VEL + green.height < HEIGHT - 10: #Bottom
        green.y += VEL
            
def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #Left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: #Right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #top
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 10: #Bottom
        red.y += VEL
        
def handle_bullets(green_bullets,red_bullets,green,red):
    for bullet in green_bullets:
        bullet.x += BULL_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            green_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            green_bullets.remove(bullet)
            
    for bullet in red_bullets:
        bullet.x -= BULL_VEL
        if green.colliderect(bullet):
            pygame.event.post(pygame.event.Event(GREEN_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
            
def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    
    green = pygame.Rect(100,300,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700,300,SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    green_bullets = []
    red_bullets = []
    
    green_health = 10
    red_health = 10
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LALT:
                    bullet = pygame.Rect(green.x + green.width, green.y + green.height//2-2,10,5)
                    green_bullets.append(bullet) 
                    BULLET_FIRE_SOUND.play()
                    
                if event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x , red.y + red.height//2-2,10,5)
                    red_bullets.append(bullet) 
                    BULLET_FIRE_SOUND.play()
                    
            if event.type == GREEN_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == RED_HIT:
                green_health -= 1    
                BULLET_HIT_SOUND.play()
            Winner_text = ""   
            if green_health <= 0:
                Winner_text= "Green wins!"  
            if red_health <= 0:
                Winner_text= "Red wins!"     
                
            if Winner_text != "":
                draw_winner(Winner_text)
                    
        keys_pressed = pygame.key.get_pressed()
        green_handle_movement(keys_pressed, green)
        red_handle_movement(keys_pressed, red)
        
        handle_bullets(green_bullets,red_bullets,green, red)
        draw_window(green, red, green_bullets, red_bullets, green_health, red_health)
        
    pygame.quit()
if __name__ == "__main__":
    main()
        