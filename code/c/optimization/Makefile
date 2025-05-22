CFLAGS=
CPPFLAGS=

SRC=$(wildcard *.c)
OUT=$(patsubst %.c,%.o,$(SRC))


all: $(OUT)

%.o : %.c
	$(CC) $(CFLAGS) $(CPPFLAGS) $< -o $@

clean:
	rm -v $(OUT)
