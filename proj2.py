#countdown timer with sound  alerts
import time
import numpy  
import sound_device 

def play_beep(frequency=1000, duration=1, samplerate=44100):
    t = numpy.linespace(0, duration, int(samplerate * duration), endpoint = False) 
    wave = 0.5 * np.sin(2 * numpy.pi *frequency * t)
    sound_device.play(wave, samplerate)
    sound_device.wait()

def countdown(seconds):
    while seconds:
        mins, secs = divmod(second,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -=1

#play beep sound
        play_beep()

        #Example usage
        countdown(10)#countdown for 10 seconds



