import sys, pygame




class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0




class GameButton:
    def __init__(self, color1, color2, color3, rect, text, pos, image = None):
        self.color = color1
        self.color_mouse_on = color2
        self.color_on_click = color3
        self.image = image
        self.rect = rect
        self.text = text
        self.pos = pos


    def mouse_on_button(self, mouse_position):
        if self.rect.right <= mouse_position[0] <= self.rect.left:
            if self.rect.bottom <= mouse_position[1] <= self.rect.top:
                return True
        return False


    def display_button(self, event, mouse_position):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, self.color_on_click, self.rect)
        elif self.mouse_on_button(mouse_position):
            pygame.draw.rect(screen, self.color_mouse_on, self.rect)

        # afficher le texte





smallfont = pygame.font.SysFont('Corbel', 35)

text = smallfont.render('quit', True, color)



size = width, height = 1250, 700



pygame.init()
screen = pygame.display.set_mode(size)
ecran_accueil = pygame.image.load("onitama.png")
screen.blit(ecran_accueil, (0, 0))
pygame.display.update()


#S1 = pygame.Surface((40, 30), screen)
button = GameButton([170, 170, 170], [100, 100, 100], [50, 50, 50], pygame.Rect(40, 30, 50, 40), 'roast LA', (40, 40))
pygame.draw.rect(screen, [100, 100, 100], button.rect)
pygame.display.update()



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.mouse_on_button(event.pos):
                pygame.draw.rect(screen, button.color_mouse_on, button.rect)
                pygame.display.update()









#pygame.init()
#pygame.init()

speed = [2, 2]
black = (0, 0, 0)

screen = pygame.display.set_mode(size)



boardgame = pygame.image.load("Boardgame.png")
ballrect = boardgame.get_rect()
screen.blit(boardgame, (0, -120))
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #ballrect = ballrect.move(speed)

    #if ballrect.left < 0 or ballrect.right > width:
        #speed[0] = -speed[0]

    #if ballrect.top < 0 or ballrect.bottom > height:
        #speed[1] = -speed[1]

    #screen.fill(black)
    #screen.blit(ball, ballrect)
    #pygame.display.flip()





