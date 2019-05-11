#ifndef _FUNCTIONS_H_
#define _FUNCTIONS_H_

#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define STR_MAX 512
#define USERLED_3 "/sys/class/leds/beaglebone:green:usr3/brightness"

typedef unsigned char byte;

byte wport(char *port_path, char *buf, int len);
byte write_byte(char *port_path, char *buf);

#endif