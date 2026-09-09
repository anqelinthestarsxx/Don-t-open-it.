define flash_time = 0.12

default flash = False
default clicks = 0
default message = ""

screen door_game():

    add "suspicious_door.png"

    # Dark overlay
    add Solid("#000000", alpha=0.7)

    # Flash overlay
    if flash:
        add Solid("#000000", alpha=0.45)

        timer 0.08 action SetVariable("flash", False)

    # Click counter
    text "[clicks] / 1000":
        xalign 0.5
        yalign 0.08
        color "#ffffff"
        size 32

    # Story/message text
    text message:
        xalign 0.5
        yalign 0.35
        xmaximum 900
        text_align 0.5
        color "#ffffff"
        size 26

    # Button
    textbutton "Click me!!":
        xalign 0.5
        yalign 0.5
        padding (40, 18)
        text_size 28
        action Function(do_click)


label start:

    scene black

    pause 0.5

    show screen door_game

    pause

    return

label ending:

    scene black

    pause 1.0

    centered "You opened it."

    pause 2.0

    centered "There was nothing inside."

    pause 2.0

    centered "..."

    pause 2.0

    centered "Until now."

    pause 3.0

    return


init python:

    def do_click():

        global clicks, message, flash

        clicks += 1

        lore = {
            100: "There was a boy here before you.",
            200: "He didn't listen to the rules.",
            300: "What are you doing?",
            400: "Do you want to leave?",
            500: "Do you really want to leave?",
            600: "He clicked it too.",
            700: "He stopped counting.",
            800: "You're not supposed to be here.",
            900: "Please don't open it."
        }

        if clicks in lore:
            message = lore[clicks]

        if clicks >= 1000:
            renpy.hide_screen("door_game")
            renpy.jump("ending")

        flash = True
        renpy.restart_interaction()