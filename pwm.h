#ifndef _PWM_H_
#define _PWM_H_

#include "functions.h"

//PWMs
#define PWM_0A "/sys/class/pwm/ehrpwm.0\\:0/"
#define PWM_0B "/sys/class/pwm/ehrpwm.0\\:1/"

#define PWM_1A "/sys/class/pwm/ehrpwm.1\\:0/"
#define PWM_1B "/sys/class/pwm/ehrpwm.1\\:1/"

#define PWM_2A "/sys/class/pwm/ehrpwm.2\\:0/"
#define PWM_2B "/sys/class/pwm/ehrpwm.2\\:1/"

#define PWM_REQUEST "request"
#define PWM_RUN		"run"
#define PWM_PERIOD	"period"
#define PWM_PERC	"duty_percent"

#endif