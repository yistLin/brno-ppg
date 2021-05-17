import struct
import sys

import numpy as np


def main():
    # assert len(sys.argv) > 1, "File paths must be provided."

    # fin = open(sys.argv[1], "rb")
    fin = open(0, "rb")
    n_samples, sample_period = struct.unpack(">ii", fin.read(8))
    sample_size, parm_kind = struct.unpack(">hh", fin.read(4))

    n_states = sample_size // 4

    print(f"[INFO] n_samples     = {n_samples}")
    print(f"[INFO] sample_period = {sample_period}")
    print(f"[INFO] sample_size   = {sample_size}")
    print(f"[INFO] parm_kind     = {parm_kind}")
    print(f"[INFO] n_states      = {n_states}")

    state_posts = np.zeros((n_samples, n_states))

    for i in range(n_samples):
        state_post = struct.unpack(">" + "f" * n_states, fin.read(sample_size))
        state_posts[i] = state_post

    print(state_posts)
    print(state_posts.shape)

    fin.close()


if __name__ == "__main__":
    main()
