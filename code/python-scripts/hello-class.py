import time
import os

t_stop = 600  # s
dt = 0
fps = 4
t = time.time()

frames = []
frames.append(
    r"        " "\n"
    r" _O/    " "\n"
    r"   \    " "\n"
    r"   /\_  " "\n"
    r"   \  ` " "\n"
    r"   `    " "\n"
)
frames.append(
    r"         " "\n"
    r"         " "\n"
    r"         " "\n"
    r"     ,   " "\n"
    r"  O/ /   " "\n"
    r"  /\|/\. " "\n"
)
frames.append(
    r"         " "\n"
    r"      ,  " "\n"
    r"     /   " "\n"
    r"  `\_\   " "\n"
    r"      \  " "\n"
    r"     /O\ " "\n"
)
frames.append(
    r"     \O_ " "\n"
    r"  ,/\/   " "\n"
    r"    /    " "\n"
    r"    \    " "\n"
    r"    `    " "\n"
    r"         " "\n"
)

index = 0
while dt < t_stop:
    os.system("clear")
    print(
        "Hello class :D! \n"
        f"Wall clock time passed: {dt:.2f} s"
        "\n\n\n"
    )
    print(frames[index])

    time.sleep(1.0/fps)
    dt = time.time() - t
    index += 1
    index = index % len(frames)
