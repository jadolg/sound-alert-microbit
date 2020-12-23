sound_level = 0
bluetooth.start_button_service()

def on_forever():
    global sound_level
    sound_level = input.sound_level()
    if sound_level > 100:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_icon(IconNames.GHOST)
    else:
        basic.clear_screen()
basic.forever(on_forever)
