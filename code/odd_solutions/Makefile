all:
	echo "hello"

logistic: logistic.so load_logistic.py
	python load_logistic.py

logistic.so: logistic/main.odin
	odin build logistic -o:speed -build-mode:dll

run_find_dups: find_dups
	./build/find_dups

find_dups: find_dups.odin
	mkdir -p build
	odin build find_dups.odin -file -o:speed -out:"./build/find_dups"
