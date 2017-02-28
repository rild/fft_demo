import numpy as np
import sys

import scipy.io.wavfile
import matplotlib.pyplot as plt

fs = 8000.0
d = 1.0 / fs
size = 256

def load_wav(filename):
    try:
        wavedata=scipy.io.wavfile.read(filename)
        samplerate=int(wavedata[0])
        wavef=wavedata[1]*(1.0/32768.0) # pcm
        if len(wavef.shape)>1: #convert to mono
            wavef=(wavef[:,0]+wavef[:,1])*0.5
        return (samplerate,wavef)
    except:
        print ("Error loading wav: "+filename)
        return None

def arg_isOk(total_time, start_time, goal_time):
    isOk = True
    if start_time < 0 or goal_time > total_time:
        isOk = False
    return isOk

def get_total_time(waveform, sampling_rate):
    return len(waveform) / float(samplerate)


def get_start_and_goal_sample_i(sampling_rate, start_time, goal_time):
    start_sample_i = float(samplerate) * start_time
    goal_sample_i = float(samplerate) * goal_time
    return (int(start_sample_i), int(goal_sample_i))

def fft_wav(waveform, sampling_rate, start_time, goal_time):

    total_time = get_total_time(waveform, sampling_rate)

    if not arg_isOk(total_time, start_time, goal_time):
        print "illegal input."
        print "start time [%d] is too early, or goal time [%d] is too late." % (start_time, goal_time)
        exit()

    print "fft start"

    # dt = np.fft.fft(waveform[1000:1000 + size]) #time frame?

    (starti, goali) = get_start_and_goal_sample_i(sampling_rate, start_time, goal_time)
    print (starti, goali)
    dt = np.fft.fft(waveform[starti:goali]) #time frame? < with sample

    size = goali - starti # frame size 

    print sampling_rate
    d = 1.0 / sampling_rate # this should be float number

    frq = np.fft.fftfreq(size, d) # But, what is the value "d"? 2/28
    print(len(frq))

    plt.subplot(2,1,1)
    plt.title("FFT - test.wav")
    plt.plot(frq, abs(dt))
    plt.axis([0, fs/2,0,max(abs(dt))])

    plt.show()

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv)

    if argc == 1:
        print "inlavid argument"
        exit()

    filename = argv[1] # "test.wav"
    (samplerate,waveform) = load_wav(filename)

    start_time = 0
    goal_time = get_total_time(waveform, samplerate)

    if argc == 4:
        start_time, goal_time = float(argv[2]), float(argv[3])

    fft_wav(waveform, samplerate, start_time, goal_time)


"""
http://ism1000ch.hatenablog.com/entry/2014/05/27/163211
http://www.ic.is.tohoku.ac.jp/~swk/lecture/yaruodsp/toc.html
http://ism1000ch.hatenablog.com/entry/2014/05/27/163211 < dominant

"""
