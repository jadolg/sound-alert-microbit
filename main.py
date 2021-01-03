sound_level = 0
sound_enabled = True
bluetooth.start_button_service()

def on_forever():
    global sound_level
    global sound_enabled
    sound_level = input.sound_level()
    if sound_level > 100:
        if sound_enabled:
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_icon(IconNames.GHOST)
    else:
        basic.clear_screen()
basic.forever(on_forever)

def on_button_pressed_a():
    global sound_enabled
    sound_enabled = not sound_enabled

input.on_button_pressed(Button.A, on_button_pressed_a)