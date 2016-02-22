# Building upon the first module that control music files
# Make sure that your rhythmbox have required plugins installed to play the song and you have some songs imported already
# Please ensure that all your songs in Music folder
# Taking text input for now . We'll change to speech soon.

from os import system

# Variables needed
music_dir="~/Music/English Music"

# Taking text input as command
input_cmd=raw_input("Enter the command : ")

#setting up the commands
cmd={'pause':"rhythmbox-client --pause"}
cmd['next']="rhythmbox-client --play \n rhythmbox-client --next"
cmd['previous']="rhythmbox-client --play \n rhythmbox-client --previous"
cmd['play']="rhythmbox-client --play"
cmd['vol-up']="rhythmbox-client --volume-up"
cmd['vol-down']="rhythmbox-client --volume-down"
cmd['hide']="rhythmbox-client --quit"
cmd['err_message']="print 'Sorry unknown command'"
cmd['quit']="rhythmbox-client --quit"

