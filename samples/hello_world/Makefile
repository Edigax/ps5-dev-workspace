# Makefile for PS5 Sample Homebrew

ELF      := hello_world.elf
TARGET   ?= $(ELF)

# Locate PS5 Payload SDK
ifndef PS5_PAYLOAD_SDK
    PS5_PAYLOAD_SDK := $(abspath ../../sdk)
endif

# Include official SDK toolchain rules if present
-include $(PS5_PAYLOAD_SDK)/toolchain/prospero.mk

CFLAGS   ?= -Wall -Wextra -O2 -g
SRC      := main.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGET) *.o

.PHONY: all clean
