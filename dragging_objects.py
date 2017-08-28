import pygame, sys

def isin(pos, rect):
    if pos[0] > rect[0] and pos[0] < rect[0]+rect[2]:
        if pos[1] > rect[1] and pos[1] < rect[1] + rect[3]: return True
        else:
            return False
    else:
        return False

Drawables = []


class Drawable:
    def __init__(self, color, rect):
        self.rect = rect
        self.color = color
        self.id = len(Drawables)
        Drawables.append(self)


pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, 0, 32)

draw1 = Drawable((255, 0, 0), [10, 10, 20, 20])
draw2 = Drawable((0, 255, 0), [20, 20, 20, 20])
draw3 = Drawable((0, 0, 255), [30, 30, 20, 20])

tracking = False
posgolb = 0
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepress = pygame.mouse.get_pressed()
                if mousepress[0] != 0:
                    pos = pygame.mouse.get_pos()
                    for drawable in Drawables:
                        if isin(pos, drawable.rect):
                            posglob = pos; drawableglob = drawable
                            tracking = True
            if event.type == pygame.MOUSEBUTTONUP:
                posglob = 0; tracking = False; drawableglob = 0

        if tracking:
            pos = pygame.mouse.get_pos()
            f = drawableglob.rect
            f[0] = pos[0] - 10
            f[1] = pos[1] - 10
            drawableglob.rect = f
        pygame.draw.rect(screen, (0,0,0),[0,0,640,480])
        for drawable in Drawables:
            pygame.draw.rect(screen, drawable.color, drawable.rect)
        pygame.display.flip()
        pygame.display.update()
