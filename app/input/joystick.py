import miio
import pygame

BUTTON_SQUARE = 0
BUTTON_X = 1
BUTTON_CIRCLE = 2
BUTTON_TRIANGLE = 3


def init_joystick():
    pygame.init()
    pygame.joystick.init()
    controller = pygame.joystick.Joystick(0)
    controller.init()
    return controller


class JoyStickControls:
    def __init__(self, bot):
        self.joystick = init_joystick()
        self.bot: miio.DreameVacuum = bot
        self.active = True

    def start(self):
        while self.active:
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == BUTTON_X:
                        self.bot.forward(300)
                    if event.button == BUTTON_SQUARE:
                        self.bot.rotate(60)
                    if event.button == BUTTON_CIRCLE:
                        self.stop()

    def stop(self):
        self.active = not self.active
        print("Shutting down.")
