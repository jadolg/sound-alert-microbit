input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    sound_enabled = !sound_enabled
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    showing_temperature = true
    basic.showNumber(input.temperature())
    showing_temperature = false
})
let sound_level = 0
let sound_enabled = false
let showing_temperature = false
bluetooth.startButtonService()
basic.forever(function on_forever() {
    
    sound_level = input.soundLevel()
    if (sound_level > 100) {
        if (sound_enabled) {
            music.playTone(262, music.beat(BeatFraction.Whole))
        }
        
        basic.showIcon(IconNames.EigthNote)
    } else if (!showing_temperature) {
        basic.clearScreen()
    }
    
})
