# -*- coding: utf-8 -*-

import sys
import wave
import pyaudio

BUF_SIZE = 1024 # samples, must be >= 64

def load_wav_data(filename):
    wavfile = wave.open(filename, 'r')

    nchannels = wavfile.getnchannels()
    sampling_rate = wavfile.getframerate()
    quantization_bits = wavfile.getsampwidth() * 8
    sample_width = wavfile.getsampwidth()
    nsamples = wavfile.getnframes()

    return (wavfile, nchannels, sampling_rate, quantization_bits, sample_width, nsamples)

def play(filename):
    (wavfile, nchannels, sampling_rate, quantization_bits, sample_width, nsamples) = load_wav_data(filename)

    print "Channels: %d" % nchannels
    print "Sampling Rate: %d Hz" % sampling_rate
    print "Quantization Bits: %d" % quantization_bits
    print "Samples: %d" % nsamples
    print "Duration: %.2f seconds" % (nsamples / float(sampling_rate))

    p = pyaudio.PyAudio()
    # 再生デバイス(スピーカやヘッドホン)と紐付けられたストリームを開く
    stream = p.open(format = p.get_format_from_width(quantization_bits / 8),
                    channels = nchannels , rate = sampling_rate , output = True)
    print "start playing "
     # BUF_SIZE ずつファイルから読み込み，ストリームに書き出す
    remain_samples = nsamples
    while remain_samples > 0:
        buf = wavfile.readframes(BUF_SIZE)
        stream.write(buf)
        remain_samples -= BUF_SIZE
    print "finish playing "


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 1:
        print "no input filies."
        exit

    filename = argv[1]
    play(filename)



"""
- 課題 1
    2 秒以内で「あいうえお」と発声し，これをサンプリング周波数 48kHz，量子化ビット数 16，モノ ラルで録音せよ.「あ・い・う・え・お」と一音ずつ区切った発音と「あーいーうーえーおー」と区切らない連 続的な発音の 2 種類を録音すること.保存した音声は必ず聴取し，音量は必要十分か，先頭や末尾が途切れて いないか，他者の音声やノイズが混入していないか，などを確認する.
- 課題 2†
    ソースコード 2 の play(filename) を拡張した play(filename, from, to) を実装せよ.例 えば，play("out.wav") は out.wav に含まれる音響信号全体を再生するのに対して，play("out.wav", 0.5, 1.0) は out.wav の 0.5 秒から 1.0 秒までを再生する.

"""


"""
module pyaudio

How to install to Mac OSX
$ brew install portaudio
$ pip install pyaudio
    portaudio.h のパスを明示的に指定しないとインストールできなかった
"""
