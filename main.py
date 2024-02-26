from pathlib import Path

from pre.slice import slice_wav

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    from os import path, listdir

    p = path.abspath(path.join(path.dirname(__file__), '.'))
    print(p)
    print(listdir(p))

    while True:
        print("SLICE WAVE PROGRAM")
        path = input("to slice wave ?")
        if path == "y":
            wav_path = str(p) + "/gdyrdqs.wav"
            slice_wav(Path(wav_path))
            print(listdir(p))
            print("FINISH!")
