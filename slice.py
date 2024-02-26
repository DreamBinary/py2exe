# -*- coding:utf-8 -*-
# @FileName : slice.py
# @Time : 2024/1/30 9:24
# @Author :fiv

from functools import partial
from multiprocessing.pool import ThreadPool
from pathlib import Path

from pydub import AudioSegment
from pydub.utils import make_chunks


def save(chunk, out_dir):
    index, chunk = chunk
    chunk_name = out_dir / f"{index:02d}.wav"
    chunk.export(chunk_name, format="wav")


def slice_wav(wave_path: Path, slice_step=30000):
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

# import time
#
# start = time.perf_counter()
# slice_wav(Path("../../data/raw/xzq/wbdqc.wav"))
# end = time.perf_counter()
# print(end - start)
# slice_wav("../../data/separate/wbdqc_vocals.wav")
