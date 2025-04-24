memtest: memtest.c
	$(CC) -O2 -o $@ $< -lpthread -msse2

clean:
	rm -f memtest