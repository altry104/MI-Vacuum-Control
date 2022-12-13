import os
import sys

from dotenv import load_dotenv

import miio

load_dotenv()


def main():

    bot = miio.DreameVacuum(
        ip=os.environ.get('IP_ADDRESS'),
        token=os.environ.get("TOKEN")
    )

    print("Bot initialized")

    input_type = sys.argv[1]

    print("Chosen control type : {}".format(input_type))

    if input_type == "joystick":
        import app.input.joystick as controls
        ctrl = controls.JoyStickControls(bot)
        ctrl.start()


main()

