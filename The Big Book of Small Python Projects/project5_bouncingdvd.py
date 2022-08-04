# This program will animate the DVD logo bouncing off the edge.
# Program use pygame module for animate, and random for first position and direction of logo

import pygame, random


#  Logo moving.
def logo_move(screen, x, y, clock):
    counter = 0
    # Create logo text.
    font = pygame.font.Font(None, 30)
    text_x = random.randint(1, x - 50)
    text_y = random.randint(25, y - 50)
    rgb = (0, 0, 0)
    # Create font for counter.
    counter_f = pygame.font.Font(None, 30)
    pygame.display.update()

    # Move text.
    speed_x = random.choice((1, -1))
    speed_y = random.choice((1, -1))
    while True:
        clock.tick(500)
        screen.fill((255, 255, 255))  # Clear screen.
        counter_t = counter_f.render(f'Corner bounces: {counter}', True, (0, 0, 0))
        screen.blit(counter_t, (25, 0))
        img = font.render('DVD', True, rgb)
        text_x += speed_x
        text_y += speed_y

        # Logo hit the edge it will change speed_x/y to opposite and change logo color to random.
        if (text_x + 45 == x or text_x == 5) and (text_y + 20 == y or text_y == 20):
            speed_x = -speed_x
            speed_y = - speed_y
            counter += 1
            rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if text_x + 45 == x or text_x == 5:
            speed_x = -speed_x
            rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if text_y + 20 == y or text_y == 20:
            speed_y = - speed_y
            rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        screen.blit(img, (text_x, text_y))
        pygame.display.update()


def main():
    pygame.init()
    clock = pygame.time.Clock()
    # Create display where logo will travel.
    x = 600
    y = 500
    screen = pygame.display.set_mode((x, y))
    pygame.display.flip()
    logo_move(screen, x, y, clock)


main()
