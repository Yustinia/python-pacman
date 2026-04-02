import pygame

from src.boards import level_one


class GameManager:
    def __init__(self, width: int = 800, height: int = 800, fps: int = 60) -> None:
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Pacman")

        self.is_running = True

    def event_handler(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass

    def runner(self) -> None:
        while self.is_running:
            self.event_handler()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()


def main() -> None:
    gm = GameManager()
    gm.runner()


if __name__ == "__main__":
    main()
