let sound_level = 0
bluetooth.startButtonService()
basic.forever(function on_forever() {
    
    sound_level = input.soundLevel()
    if (sound_level > 100) {
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.showIcon(IconNames.Ghost)
    } else {
        basic.clearScreen()
    }
    
})
