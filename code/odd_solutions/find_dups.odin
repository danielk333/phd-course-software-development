package main

import "core:fmt"
import "core:os"
import "core:slice"
import "core:hash/xxhash"

main :: proc() {
    fmt.println("Finding duplicate files")
    path := "./a_few_files"
    fh, err := os.open(path)
    if err != os.ERROR_NONE {
        fmt.eprintln("Count not open path", err)
        os.exit(1)
    }
    defer os.close(fh)

	files, err_dir := os.read_dir(fh, -1)
	if err_dir != os.ERROR_NONE {
		fmt.eprintln("Could not read directory", err)
		os.exit(1)
	}

    seed: u64 = 0
    hash: u64
    hashes: map[u64][dynamic]int
    for ind in 1..<len(files) {
        fmt.printfln("reading {:v}", files[ind].name)
        data, ok := os.read_entire_file_from_filename(files[ind].fullpath)
        if !ok {
            fmt.eprintln("Failed to read the file")
            os.exit(1)
        }
        hash = xxhash.XXH64(data, seed)
        if hash in hashes {
            append(&hashes[hash], ind)
        }
        else {
            hashes[hash] = make([dynamic]int, 1, len(files))
            hashes[hash][0] = ind
        }
        fmt.printfln("hash {:v}", hash)
    }
    for key in hashes {
        fmt.printfln("{:v} = {:v}", key, hashes[key])
    }
}
