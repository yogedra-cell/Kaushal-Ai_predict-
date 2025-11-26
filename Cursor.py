import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

Input = {
    "mouse": {
        "left": False,
        "middle": False,
        "right": False
    }
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:      # left click
                Input["mouse"]["left"] = True
            if event.button == 2:      # middle click
                Input["mouse"]["middle"] = True
            if event.button == 3:      # right click
                Input["mouse"]["right"] = True

        # Mouse button up
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Input["mouse"]["left"] = False
            if event.button == 2:
                Input["mouse"]["middle"] = False
            if event.button == 3:
                Input["mouse"]["right"] = False

    screen.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
