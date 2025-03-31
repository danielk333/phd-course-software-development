run_find_dups: find_dups
	./build/find_dups

find_dups: find_dups.odin
	mkdir -p build
	odin build find_dups.odin -file -o:speed -out:"./build/find_dups"
