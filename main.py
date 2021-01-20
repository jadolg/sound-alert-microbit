def on_button_pressed_a():
    global sound_enabled
    sound_enabled = not (sound_enabled)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global showing_temperature
    showing_temperature = True
    basic.show_number(input.temperature())
    showing_temperature = False
input.on_button_pressed(Button.B, on_button_pressed_b)

sound_level = 0
sound_enabled = False
showing_temperature = False

bluetooth.start_button_service()

def on_forever():
    global sound_level, showing_temperature
    sound_level = input.sound_level()
    if sound_level > 100:
        if sound_enabled:
            music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.show_icon(IconNames.EIGTH_NOTE)
    else:
        if not showing_temperature:
            basic.clear_screen()
basic.forever(on_forever)
