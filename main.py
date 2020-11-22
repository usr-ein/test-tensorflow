#!/usr/bin/env python3
"""Execute test commands in Tensorflow to see if it manages to access the GPU(s)"""
from colorama import init, Fore, Back, Style  # type: ignore


def main():
    """Main function"""
    init(autoreset=True)  # For colorama
    print(Style.BRIGHT + Fore.RED + " Testing if Tensorflow works...")

    print(Fore.RED + "Tries listing the GPUs")
    from tensorflow.python.client import device_lib  # type: ignore

    d = device_lib.list_local_devices()
    print(Style.DIM + Fore.LIGHTGREEN_EX + str(d))
    print("\n")
    print(Fore.GREEN + "OK")

    print(Fore.RED + "Tries computing a small thing on the GPUs")
    import tensorflow as tf  # type: ignore

    print(Style.DIM + Fore.LIGHTGREEN_EX + str(tf.reduce_sum(tf.random.normal([1000, 1000]))))
    print(Fore.GREEN + "OK")

    print(Style.BRIGHT + Fore.GREEN + "Everything is in order\033[00m")


# docker run --gpus all -it --rm tensorflow/tensorflow:nightly-gpu

if __name__ == "__main__":
    main()
