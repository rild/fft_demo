# _*_ coding: utf-8 _*_

import sys
import pyaudio
import wave

SAMPLING_RATE = 48000 # Hz
QUANTIZATION_BITS = 16 # Bits
CHANNELS = 1 # monoral

# 録音用のバッファのサイズ.単位はサンプル
# バッファサイズ・遅延・音飛びには以下の関係がある
# ハードウェアやアプリケーションに合わせた適切な値の設定が必要
# ----------
# Buffer size   |   larger  ---     smaller
# Delay         |   smaller ---     larger
# Skipping      |   occuring ---
# Delay and Skipping are trade-off ...?

BUF_SIZE = 1024

def record(seconds, filename):
    # open wav file, and write some data; format
    wavfile = wave.open(filename, 'wb')
    wavfile.setframerate(SAMPLING_RATE)
    wavfile.setsampwidth(QUANTIZATION_BITS / 8)
    wavfile.setnchannels(CHANNELS)

    p = pyaudio.PyAudio()

    # open stream related to recoding device(micro phone)
    stream = p.open(format = p.get_format_from_width(QUANTIZATION_BITS / 8),
                    channels = CHANNELS,
                    rate = SAMPLING_RATE,
                    input = True,
                    frames_per_buffer = BUF_SIZE)

    print "start recoding"
    # read data of stream by BUF_SIZE, and write that to file
    remain_samples = int(SAMPLING_RATE * seconds)

    while remain_samples > 0:
        print remain_samples
        # data = stream.read(min(BUF_SIZE * remain_samples))
        data = stream.read(min(BUF_SIZE, remain_samples))
        print data
        wavfile.writeframes(data)
        remain_samples -= BUF_SIZE
    print "finish recoding"

    wavfile.close()
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    argv = sys.argv

    if len(argv) != 3:
        print "Invalid arguments."
        print "Usage: python record.py <record_seconds> <filename>"
        exit()

    record_seconds = argv[1]
    output_filename = argv[2]

    record(float(record_seconds), output_filename)
