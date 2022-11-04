# from pygame import mixer
# mixer.init() 
# sound=mixer.Sound("sounds/crash.wav")
# sound.play()

import simpleaudio 
crash = simpleaudio.WaveObject.from_wave_file("sounds/crash.wav")
highHat = simpleaudio.WaveObject.from_wave_file("sounds/hi hat.wav")
kick = simpleaudio.WaveObject.from_wave_file("sounds/kick.wav")
snare = simpleaudio.WaveObject.from_wave_file("sounds/snare.wav")
tom = simpleaudio.WaveObject.from_wave_file("sounds/tom.wav")
clap = simpleaudio.WaveObject.from_wave_file("sounds/clap.wav")



instruments = {
    "RED": tom,
    "BLUE": highHat,
    "GREEN": clap
}

def getSound(color):
    if color in instruments:
        play_obj = instruments[color].play()
        play_obj.wait_done()
    return

if __name__ == "__main__":
    # Test function
    getSound("RED")

    # Test sounds
    play_obj = highHat.play()
    play_obj.wait_done()

    play_obj = crash.play()
    play_obj.wait_done()

    play_obj = tom.play()
    play_obj.wait_done()

    play_obj = clap.play()
    play_obj.wait_done()
