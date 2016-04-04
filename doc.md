| /do/led/blink                                   |                                                                                                          |
|:------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| Info                                            | [beta] [gpio] [led] [electronics]                                                                        |
| Description                                     | Blink a led                                                                                              |
| Usage                                           | /do/led/blink pin or /do/led/blink pin number_of_times or /do/led/blink pin number_of_times speed (in s) |
| Example                                         | /do/led/blink 21 or /do/led/blink 21 3 /do/led/blink 21 3 0.1                                            |
| Arguments                                       | 1:ledPin, 2:loopUntil, 2:loopUntil, 3:speed,                                                             |
| Variables                                       | ledPin=$1, loopUntil=$2, loopUntil=$2, speed=$3,                                                         |
| Modules                                         | /do/led/python/blink.py $ledPin $loopUntil $speed,                                                       |
| 1. Could you tell me where the led is plugged ? |                                                                                                          |
| 2. Blink LED $ledPin                            |                                                                                                          |

| /do/led/install   |                                   |
|:------------------|:----------------------------------|
| Info              | [beta] [gpio] [led] [electronics] |
| Description       | Install led module (wiringPi)     |
| Usage             | /do/led/install                   |
| Softwares         | WiringPi,                         |
| System            | /system/installWiringPi,          |
| 1. [LED] Install  |                                   |

| /do/led/off                                     |                                    |
|:------------------------------------------------|:-----------------------------------|
| Info                                            | [beta] [gpio] [led] [electronics]  |
| Description                                     | Turn off a led                     |
| Usage                                           | /do/led/off pin                    |
| Example                                         | /do/led/off 21                     |
| Arguments                                       | 1:ledPin,                          |
| Variables                                       | ledPin=$1,                         |
| Modules                                         | /do/led/python/onoff.py $ledPin 0, |
| 1. Turn off LED $ledPin                         |                                    |
| 2. Could you tell me where the led is plugged ? |                                    |

| /do/led/on                                      |                                    |
|:------------------------------------------------|:-----------------------------------|
| Info                                            | [beta] [gpio] [led] [electronics]  |
| Description                                     | Turn off a led                     |
| Usage                                           | /do/led/on pin                     |
| Example                                         | /do/led/on 21                      |
| Arguments                                       | 1:ledPin,                          |
| Variables                                       | ledPin=$1,                         |
| Modules                                         | /do/led/python/onoff.py $ledPin 1, |
| 1. Turn off LED $ledPin                         |                                    |
| 2. Could you tell me where the led is plugged ? |                                    |

| /do/led/pulse                                   |                                              |
|:------------------------------------------------|:---------------------------------------------|
| Info                                            | [beta] [gpio] [led] [electronics]            |
| Description                                     | Software PWM with led                        |
| Usage                                           | /do/led/pulse pin or /do/led/pulse pin speed |
| Example                                         | /do/led/pulse 21 or /do/led/pulse 21 1       |
| Arguments                                       | 1:ledPin, 2:speed,                           |
| Variables                                       | ledPin=$1, speed=$2,                         |
| Modules                                         | /do/led/python/pulse.py $ledPin $speed,      |
| 1. Could you tell me where the led is plugged ? |                                              |
| 2. Pulse LED $ledPin                            |                                              |