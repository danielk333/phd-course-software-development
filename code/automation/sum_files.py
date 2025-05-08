from pathlib import Path
from snakemake.script import snakemake

total = 0
for file in snakemake.input:
    total += Path(file).stat().st_size

with open(snakemake.output[0], "wb") as fh:
    fh.write(total.to_bytes())
