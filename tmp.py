# -*- coding:utf-8 -*-
# @FileName : tmp.py
# @Time : 2024/2/13 14:18
# @Author : fiv
from functools import partial
from multiprocessing.pool import ThreadPool
from pathlib import Path

from numba import jit
from pydub import AudioSegment
from pydub.utils import make_chunks



def save(chunk, out_dir):
    index, chunk = chunk
    chunk_name = out_dir / f"{index:02d}.wav"
    chunk.export(chunk_name, format="wav")

@jit
def slice_wav(slice_step=30000):
    wave_path = Path(__file__).parent / "pre" / "gdyrdqs.wav"
    audio = AudioSegment.from_file(wave_path, "wav")
    out_dir = Path(__file__).parent / wave_path.stem
    print("out_dir:", out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks = make_chunks(audio, slice_step)
    chunks = list(zip(range(len(chunks)), chunks))
    save_p = partial(save, out_dir=out_dir)

    # with multiprocessing.Pool() as pool:
    #     pool.map(save_p, chunks)

    with ThreadPool() as pool:
        pool.map(save_p, chunks)


# @jit
def slice_wav(slice_step=30000):
    wave_path = Path(__file__).parent / "pre" / "gdyrdqs.wav"
    audio = AudioSegment.from_file(wave_path, "wav")
    out_dir = Path(__file__).parent / wave_path.stem
    print("out_dir:", out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    chunks = make_chunks(audio, slice_step)
    chunks = list(zip(range(len(chunks)), chunks))
    save_p = partial(save, out_dir=out_dir)

    # with multiprocessing.Pool() as pool:
    #     pool.map(save_p, chunks)

    with ThreadPool() as pool:
        pool.map(save_p, chunks)


if __name__ == '__main__':
    import time

    start = time.perf_counter()
    slice_wav()
    end = time.perf_counter()
    print(end - start)

    # start = time.perf_counter()
    # slice_wav()
    # end = time.perf_counter()
    # print(end - start)
# out_dir: /root/py2exe/gdyrdqs
# 0.07971709400044347
