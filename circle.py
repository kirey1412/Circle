import pygame
pygame.init()
window=pygame.display.set_mode((420,400))
window.fill("lightyellow")
pygame.display.update()

class Circle():
    def __init__(self, dimension):
        #self.color=color
        self.surface=window
        self.cirdimension=dimension
    def draw(self):
        pygame.draw.circle(self.surface, self.cirdimension[3], (self.cirdimension[3], self.cirdimension[1]), self.cirdimension[2])
pinkcircle=Circle((200,200, 50, "pink"))
pinkcircle.draw()

bluecircle=Circle((250, 250, 50, "blue"))
bluecircle.draw()

pygame.display.update()
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            break
pygame.quit()