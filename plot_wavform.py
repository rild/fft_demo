# _*_ coding: utf-8 _*_

import sys
import scipy.io.wavfile
import numpy
import pylab

def plot_waveform(waveform, sampling_rate):
    times = numpy.arange(float(len(waveform))) / sampling_rate # 各サンプルの時刻

    pylab.plot(times, waveform) # pair of x- and y-coordinate lists/arrays
    pylab.title("Waveform")
    pylab.xlabel("Time[sec]")
    pylab.ylabel("Amplitude")
    pylab.xlim([0, len(waveform) / sampling_rate])
    pylab.ylim([-1, 1])
    pylab.show()

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        print "no input files."
        exit()

    filename = argv[1]
    sampling_rate, waveform = scipy.io.wavfile.read(filename)
    # WAVファイルのフォーマットが符号あり16bit整数であることを仮定する
    # 波形が -1.0 ~ 1.0 の範囲に収まるように正規化を行う

waveform = waveform / 32768.0 # pcm?
plot_waveform(waveform, sampling_rate)
