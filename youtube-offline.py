import re
from pathlib import Path

pattern = re.compile(r"[<][\s]+(youtube)[\s]+([a-zA-Z0-9]+)[\s]+[>]")

d = Path("content")
md_files = d.rglob("*.md")

all_links = []
for file in md_files:
    print(file)
    with open(file, "r") as fh:
        matches = [
            pattern.search(line)
            for line in fh.readlines()
        ]
        matches = [x.group(2) for x in matches if x is not None]
    all_links += matches

for key in all_links:
    print(f"yt-dlp  https://www.youtube.com/watch?v={key}")
