from pathlib import Path
import random
import string
from snakemake.script import snakemake


def make_file(path, ind, ext):
    with open(path / f"{ind}{ext}", "w") as fh:
        fh.write(
            "".join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=random.randint(1, 257),
                )
            )
        )


path = Path(snakemake.input[0])
make_file(path, "data", ".dat")
make_file(path, "data", ".txt")
