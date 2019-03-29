import random
import pygame

BLACK = (0,0,0)
WHITE = (255, 255, 255)


EKRAN_SIRINA = 700
EKRAN_VISINA = 500
VELICINA_LOPTE = 25


class Loptica:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_promjena = 0
        self.y_promjena = 0


def napravi_lopticu():
    loptica = Loptica()
    loptica.x = random.randrange(VELICINA_LOPTE, EKRAN_SIRINA-VELICINA_LOPTE)
    loptica.y = random.randrange(VELICINA_LOPTE, EKRAN_VISINA-VELICINA_LOPTE)

    loptica.x_promjena = random.randrange(-3, 3)
    loptica.y_promjena = random.randrange(-3, 3)

    return loptica

def main():
    pygame.init()
    
    ekran = pygame.display.set_mode([EKRAN_SIRINA, EKRAN_VISINA])
    sat = pygame.time.Clock()

    lista_loptica = []
    loptica = napravi_lopticu()
    lista_loptica.append(loptica)
    
    gotovo = False

    while not gotovo:
        ekran.fill(BLACK)

        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                gotovo = True
            elif dogadjaj.type == pygame.KEYDOWN:
                if dogadjaj.key == pygame.K_SPACE:
                    loptica = napravi_lopticu()
                    lista_loptica.append(loptica)

        for loptica in lista_loptica:
            loptica.x += loptica.x_promjena
            loptica.y += loptica.y_promjena

            if loptica.y >= EKRAN_VISINA-VELICINA_LOPTE or loptica.y < VELICINA_LOPTE:
                loptica.y_promjena *= -1

            if loptica.x >= EKRAN_SIRINA-VELICINA_LOPTE or loptica.x < VELICINA_LOPTE:
                loptica.x_promjena *= -1
        
        for loptica in lista_loptica:
            pygame.draw.circle(ekran, WHITE, [loptica.x, loptica.y], VELICINA_LOPTE)
        sat.tick(21)
        pygame.display.flip()
    pygame.quit()

main()