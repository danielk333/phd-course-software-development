CFLAGS=-lm

SRC=$(wildcard *_o0.c)
SRC_OPT=$(wildcard *_o3.c)
OUT=$(patsubst %.c,%.o,$(SRC))
OUT_OPT=$(patsubst %.c,%.o,$(SRC_OPT))


all: $(OUT) $(OUT_OPT)

%_o0.o : %_o0.c
	$(CC) $(CFLAGS) $< -o $@

%_o3.o : %_o3.c
	$(CC) -O3 $(CFLAGS) $< -o $@

clean:
	rm -v $(OUT) $(OUT_OPT)
