all:
	$(CC) -lm shaving_op_without.c -o shaving_op_without.o
	$(CC) -lm shaving_op_with.c -o shaving_op_with.o
	$(CC) -O3 -lm shaving_op_with.c -o shaving_op_with_o3.o
	$(CC) -O3 -lm shaving_op_without.c -o shaving_op_without_o3.o
	$(CC) -mavx512f with_simd.c -o with_simd.o
	$(CC) -O3 -mavx512f with_simd.c -o with_simd_o3.o
	$(CC) without_simd.c -o without_simd.o
	$(CC) -O3 without_simd.c -o without_simd_o3.o
	$(CC) branch_miss.c -o branch_miss.o
	$(CC) no_branch_miss.c -o no_branch_miss.o

clean:
	rm -v *.o
