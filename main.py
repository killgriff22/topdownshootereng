from classes import *
player = Player(0,0,10,10, (0,0,255))
img = pygame.image.load("world.png")
world = World(0,10,img)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #write a wrapper for pygame.key.get_pressed() that lets you use the arrow keys and wasd
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        world.y -= 1
    if keys[pygame.K_s]:
        world.y += 1
    if keys[pygame.K_a]:
        world.x -= 1
    if keys[pygame.K_d]:
        world.x += 1
    if world.collide_color(player,(0,0,0)):
        distances,points = [],[]
        for direction in [(0,1),(0,-1),(1,0),(-1,0)]:
            tmpx,tmpy = world.x,world.y
            while not world.collide_color(player,(0,0,0)):
                world.x += direction[0]
                world.y += direction[1]
            distances.append(math.sqrt((world.x-player.x)**2+(world.y-player.y)**2))
            points.append((world.x,world.y))
            world.x,world.y = tmpx,tmpy
        world.x,world.y = points[distances.index(min(distances))]
        print(points[distances.index(min(distances))])
    else:
        print("doesn't collide")
    Screen.blit(world.image, (world.x,world.y))
    pygame.draw.rect(Screen, (0,0,255), (0,0,10,10))
    pygame.display.flip()
