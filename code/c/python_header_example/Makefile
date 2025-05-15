CFLAGS=$(shell python-config --cflags) -fPIC -shared
INCLUDES=$(shell python-config --includes)

build:
	gcc $(INCLUDES) $(CFLAGS) bar.c -o bar.so
