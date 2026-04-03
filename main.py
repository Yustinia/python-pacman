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

        board_width, board_height = (
            self.width // len(self.board[0]),
            self.height // len(self.board),
        )
        self.tile_size = min(board_width, board_height)

    def draw(self, screen):
        pellet_rad = 4
        pellet_color = (200, 200, 200)
        line_thickness = 4
        line_color = (40, 40, 200)
        arc_pi = pi

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                center_x = j * self.tile_size + self.tile_size // 2
                center_y = i * self.tile_size + self.tile_size // 2

                if self.board[i][j] == 1:
                    pygame.draw.circle(
                        screen, pellet_color, (center_x, center_y), pellet_rad
                    )

                if self.board[i][j] == 2:
                    pygame.draw.line(
                        screen,
                        line_color,
                        (center_x, center_y - self.tile_size // 2),
                        (center_x, center_y + self.tile_size // 2),
                        line_thickness,
                    )

                if self.board[i][j] == 3:
                    pygame.draw.line(
                        screen,
                        line_color,
                        (center_x - self.tile_size // 2, center_y),
                        (center_x + self.tile_size // 2, center_y),
                        line_thickness,
                    )

                if self.board[i][j] == 4:
                    pygame.draw.arc(
                        screen,
                        line_color,
                        (
                            center_x,
                            center_y,
                            self.tile_size,
                            self.tile_size,
                        ),
                        arc_pi / 2,
                        arc_pi,
                        line_thickness,
                    )

                if self.board[i][j] == 5:
                    pygame.draw.arc(
                        screen,
                        line_color,
                        (
                            center_x - self.tile_size,
                            center_y,
                            self.tile_size,
                            self.tile_size,
                        ),
                        arc_pi * 2,
                        arc_pi / 2,
                        line_thickness,
                    )

                if self.board[i][j] == 6:
                    pygame.draw.arc(
                        screen,
                        line_color,
                        (
                            center_x,
                            center_y - self.tile_size,
                            self.tile_size,
                            self.tile_size,
                        ),
                        arc_pi,
                        (3 * arc_pi) / 2,
                        line_thickness,
                    )

                if self.board[i][j] == 7:
                    pygame.draw.arc(
                        screen,
                        line_color,
                        (
                            center_x - self.tile_size,
                            center_y - self.tile_size,
                            self.tile_size,
                            self.tile_size,
                        ),
                        (3 * arc_pi) / 2,
                        arc_pi * 2,
                        line_thickness,
                    )


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

    def draw(self, screen):
        self.background.draw(screen)
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
