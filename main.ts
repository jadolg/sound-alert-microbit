input.onButtonPressed(Button.A, function () {
    sound_enabled = !(sound_enabled)
})
let sound_level = 0
let sound_enabled = false
sound_enabled = true
bluetooth.startButtonService()
basic.forever(function () {
    sound_level = input.soundLevel()
    if (sound_level > 100) {
        if (sound_enabled) {
            music.playTone(262, music.beat(BeatFraction.Whole))
        }
        basic.showIcon(IconNames.EigthNote)
    } else {
        basic.clearScreen()
    }
})
