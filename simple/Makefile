TARGETR=lora_receiver
TARGETS=lora_sender

CC=gcc
CXX=g++
RM=rm -f

INCLUDES_PATH=-I lib/
CPPFLAGS=-std=c++11 -g -Wall -DRH_PLATFORM=RH_PLATFORM_RPI -D__RASPBERRY_PI_ $(INCLUDES_PATH)
CFLAGS=-g -Wall -DRH_PLATFORM=RH_PLATFORM_RPI -D__RASPBERRY_PI_ $(INCLUDES_PATH)
LDFLAGS=-lwiringPi

RH95_SRCS=lib/RH_RF95.cpp \
	lib/RHGenericSPI.cpp \
	lib/RHLinuxSPI.cpp \
 	lib/RHGenericDriver.cpp
RH95_OBJS=$(subst .cpp,.o,$(RH95_SRCS))

all: $(TARGETR) $(TARGETS)

$(TARGETR): src/receiver.o $(RH95_OBJS)
	$(CXX) $(LDFLAGS) -o $@ $^

$(TARGETS): src/sender.o $(RH95_OBJS)
	$(CXX) $(LDFLAGS) -o $@ $^

%.o: %.cpp
	$(CXX) $(CPPFLAGS) -o $@ -c $<
%.o: %.c
	$(CC) $(CFLAGS) -o $@ -c $<

clean:
	$(RM) $(TARGETR) $(TARGETS) $(RH95_OBJS) src/receiver.o src/sender.o

