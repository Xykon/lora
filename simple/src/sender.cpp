/*
Original code by: https://github.com/Snootlab/lora_chisterapi
Edited by: Ramin Sangesari
*/

/*-----------------------------------------*/
#include <dirent.h>
#include <string.h>
#include <fcntl.h>
/*-----------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <RH_RF95.h>

RH_RF95 rf95;

/* The address of the node which is 10 by default */
uint8_t node_number = 7;
uint8_t msg[3] = {0,0,0};
int run = 1;
/*-----------------------------------------*/
ssize_t numRead;
/*-----------------------------------------*/


/* Send a message every 3 seconds */
void sigalarm_handler(int signal)
{
    msg[0] = node_number;
    msg[1]++;
    msg[2] = 0xab;
 
    rf95.send(msg, sizeof(msg));
    rf95.waitPacketSent();
    printf("Send 0x%x 0x%x 0x%x\n",msg[0],msg[1],msg[2]);
    alarm(3);
}

/* Signal the end of the software */
void sigint_handler(int signal)
{
    run = 0;
}

void setup()
{ 

    wiringPiSetupGpio();

    if (!rf95.init()) 
    {
        fprintf(stderr, "Init failed\n");
        exit(1);
    }

    /* Tx power is from +5 to +23 dBm */
    rf95.setTxPower(23);
    /* There are different configurations
     * you can find in lib/radiohead/RH_RF95.h 
     * at line 437 
     */
    rf95.setModemConfig(RH_RF95::Bw125Cr45Sf128);
    rf95.setFrequency(868.1); /* Mhz */
}

void loop()
{
	sleep(1000);
}

int main(int argc, char **argv)
{
    signal(SIGINT, sigint_handler);
    signal(SIGALRM, sigalarm_handler);

    alarm(3);

    setup();

    while( run )
    {
        loop();
        usleep(5);
    }

    return EXIT_SUCCESS;
}
