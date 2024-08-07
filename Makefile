
all: bitfont

bitfont: bitfont.o example.o
	$(CC) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) -o $@ -c $^ $(CFLAGS)

bitfont.c: font.py
	./font.py > $@

bitfont.py: font.py
	./font.py -py > $@

clean:
	rm -f bitfont *.o bitfont.c
