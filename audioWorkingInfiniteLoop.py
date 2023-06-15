import time 
import os
import sounddevice as sd
from scipy.io.wavfile import write


fs = 44100  # Sample rate
neo=''
files_to_keep=5
file_length = 5  # Duration of recording
saveNum=2
save=False
while True:
  t=time.time()
  t=t-t%file_length#rounds to thre nearest interval

  myrecording = sd.rec(int(file_length * fs), samplerate=fs, channels=2)#starts recording
  sd.wait()  # Wait until recording is finished

  write(str(t)+'.wav', fs, myrecording)  # Save as WAV file

  if os.path.exists(str(t-(file_length*files_to_keep))+'.wav'):#checks if the deletion target exists
    os.remove(str(t-(file_length*files_to_keep))+'.wav')#deletes the file that is the oldest
  else:
    print("The file does not exist",str(t-(file_length*files_to_keep))+'.wav')
