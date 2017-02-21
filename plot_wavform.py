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

def plt_wav(waveform, sampling_rate, start_time, goal_time):
    times = numpy.arange(float(len(waveform))) / sampling_rate # 各サンプルの時刻
    # new_times = []
    # frames = []
    # # ここ for 文ではない処理に変えたい..
    # for i in range(0, len(times)):
    #     if times[i] > start_time and times[i] < goal_time:
    #         new_times.append(times[i])
    #         frames.append(waveform[i])

    xlimit =  len(waveform) / sampling_rate

    pylab.plot(times, waveform) # pair of x- and y-coordinate lists/arrays
    pylab.title("Waveform")
    pylab.xlabel("Time[sec]")
    pylab.ylabel("Amplitude")
    pylab.xlim([start_time, goal_time])
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

    if len(argv) == 4:
        start = float(argv[2])
        goal = float(argv[3])
        plt_wav(waveform, sampling_rate, start, goal)
    else:
        plot_waveform(waveform, sampling_rate)
