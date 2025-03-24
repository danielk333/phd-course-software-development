from pathlib import Path
import random

TARGET = Path(".") / "a_few_files"
FILES_N = 69
random.seed(323847)

content = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
]

file_content = [
    "\n".join(random.sample(content, k=2))
    for ind in range(FILES_N)
]
filenames = [
    f"{ind}_{ind % 3}.txt"
    for ind in range(FILES_N)
]

if __name__ == "__main__":
    if TARGET.is_file():
        raise FileExistsError(f"{TARGET=} already exists as a file")
    TARGET.mkdir(exist_ok=True)

    for fname, content in zip(filenames, file_content):
        file = TARGET / fname
        with open(file, "w") as fh:
            fh.write(content)
