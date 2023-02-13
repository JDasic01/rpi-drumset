# rpi-drumset

## Presets
Preset name should be 1_Name, for example

1_Rock
2_Metal
3_Jazz

these names should be created as a folder in the directory "sounds", so creating a new sound in the mobile app should result in a folder that is a subdirectory of sounds.

Examples:
preset "Rock" should be in sounds/1_Rock
the number will be used for sorting sounds in the rPi drum module.

under the folder sounds/1_Rock there should be sounds
snare.wav
kick.wav
tom-hi.wav
tom-mid.wav
tom-low.wav
crash.wav
ride.wav
- not all are neccesary, names can be changed but they need to be the same between directories
Drum module will get the sounds based on folders in the folder sounds, so the name can be anything but it should have a number as a prefix so the user can modify the order of sounds.

