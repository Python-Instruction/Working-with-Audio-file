
#source file
src='/content/gdrive/My Drive/working/speaker/speaker_1_2.mp3'
#destination 
dst='/content/gdrive/My Drive/working/speaker/speaker_1_2.wav'
from os import path
from pydub import AudioSegment

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

