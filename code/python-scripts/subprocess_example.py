import subprocess

addrs = "192.167.0.{:d}"
prog = "ping "
opts = "-c 1 "

processes = []
for ind in range(256):
    cmd = " ".join(["ping", f"192.167.0.{ind:d}", "-c", "1"])
    print(f"starting '{cmd}'")
    p = subprocess.Popen(cmd, cwd="/", shell=True)
    processes.append(p)

for p in processes:
    p.wait()
