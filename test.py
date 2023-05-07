from pygame import mixer, _sdl2 as devicer

mixer.init() # Initialize the mixer, this will allow the next command to work

# Returns playback devices, Boolean value determines whether they are Input or Output devices.
print("Inputs:", devicer.audio.get_audio_device_names(True))
print("Outputs:", devicer.audio.get_audio_device_names(False))