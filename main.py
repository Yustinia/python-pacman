import pygame

from src.boards import level_one


class Background:
    def __init__(self, width: int, height: int, color: tuple[int, int, int]) -> None:
        self.width = width
        self.height = height
        self.color = color

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(0, 0))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Pellet(pygame.sprite.Sprite):
    def __init__(
        self,
        coord_x: int,
        coord_y: int,
        color: tuple[int, int, int],
        radius: int = 5,
    ) -> None:
        super().__init__()

        self.radius = radius
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.color = color

        self.image = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(self.image, self.color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(coord_x, coord_y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Board:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.board = level_one.copy()

        bg_clr = (10, 10, 20)
        self.background = Background(self.width, self.height, bg_clr)

        self.pellets = pygame.sprite.Group()
        board_wd, board_ht = self.width // len(self.board[0]), self.height // len(
            self.board
        )

        pellet_color = (200, 200, 200)
        power_pellet_color = (255, 40, 40)
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pellet_pos = (
                    j * board_wd + board_wd // 2,
                    i * board_ht + board_ht // 2,
                )

                if self.board[i][j] == 1:
                    self.pellets.add(Pellet(pellet_pos[0], pellet_pos[1], pellet_color))

                if self.board[i][j] == 2:
                    self.pellets.add(
                        Pellet(
                            pellet_pos[0], pellet_pos[1], power_pellet_color, radius=10
                        )
                    )

    def draw(self, screen):
        self.background.draw(screen)

        for pellet in self.pellets:
            pellet.draw(screen)


class Game:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.board = Board(self.width, self.height)

    def draw(self, screen):
        self.board.draw(screen)


class GameManager:
    def __init__(self, width: int = 800, height: int = 800, fps: int = 60) -> None:
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pacman")

        self.is_running = True

        # objects
        self.game = Game(self.width, self.height)

    def event_handler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self) -> None:
        pass

    def draw(self) -> None:
        self.game.draw(self.screen)

    def runner(self) -> None:
        while self.is_running:
            self.event_handler()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
            pygame.display.update()

        pygame.quit()


def main() -> None:
    gm = GameManager()
    gm.runner()


if __name__ == "__main__":
    main()
