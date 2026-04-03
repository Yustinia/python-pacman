from math import pi

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


class Board:
    def __init__(self, width: int, height: int, board) -> None:
        self.width = width
        self.height = height
        self.board = board

    def draw(self, screen):
        pellet_rad = 4
        pellet_color = (200, 200, 200)

        power_pellet_rad = pellet_rad * 2
        power_pellet_color = (200, 200, 50)

        rect_color = (40, 40, 200)
        wall_padding = 4

        board_wd, board_ht = (
            self.width // len(self.board[0]),
            self.height // len(self.board),
        )

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 1:
                    pygame.draw.circle(
                        screen,
                        pellet_color,
                        (
                            j * board_wd + board_wd // 2,
                            i * board_ht + board_ht // 2,
                        ),
                        pellet_rad,
                    )

                if self.board[i][j] == 2:
                    pygame.draw.circle(
                        screen,
                        power_pellet_color,
                        (j * board_wd + board_wd // 2, i * board_ht + board_ht // 2),
                        power_pellet_rad,
                    )

                if self.board[i][j] == 3:
                    pygame.draw.rect(
                        screen,
                        rect_color,
                        (
                            j * board_wd + wall_padding,
                            i * board_ht + wall_padding,
                            board_wd - 2 * wall_padding,
                            board_ht - 2 * wall_padding,
                        ),
                    )


class Player:
    def __init__(self, width: int, height: int, speed: int = 5) -> None:
        self.width = width
        self.height = height
        self.speed = speed

        self.image = pygame.Surface((20, 20))
        self.image.fill((200, 200, 50))
        self.rect = self.image.get_rect(center=(self.width // 2, self.height // 2))

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Game:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        bg_color = (10, 10, 20)
        self.background = Background(
            self.width,
            self.height,
            bg_color,
        )

        self.board = Board(self.width, self.height, level_one)
        self.player = Player(self.width, self.height)

    def draw(self, screen):
        self.background.draw(screen)
        self.board.draw(screen)
        self.player.draw(screen)


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
