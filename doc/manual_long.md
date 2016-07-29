| /do/led/blink                                   |                                                                                                               |
|:------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| Info                                            | [beta] [gpio] [led] [electronics] [orangepi]                                                                  |
| Description                                     | Blink a led                                                                                                   |
| Usage                                           | /do/led/blink pin or /do/led/blink pin number_of_times or /do/led/blink pin number_of_times speed (in s)      |
| Example                                         | /do/led/blink 21 or /do/led/blink 21 3 /do/led/blink 21 3 0.1                                                 |
| Arguments                                       | 1:ledPin, 2:loopUntil, 2:loopUntil, 3:speed,                                                                  |
| Variables                                       | hardware=$(/pi/getBoard), ledPin=$1, loopUntil=$2, loopUntil=$2, speed=$3, ledPin=$(/system/h3ToBcm $ledPin), |
| Modules                                         | /do/led/python/blink_orange.py $ledPin $loopUntil $speed, /do/led/python/blink.py $ledPin $loopUntil $speed,  |
| System                                          | ledPin=$(/system/h3ToBcm $ledPin),                                                                            |
| 1. Could you tell me where the led is plugged ? |                                                                                                               |
| 2. Blink LED $ledPin                            |                                                                                                               |

| /do/led/install                    |                                                      |
|:-----------------------------------|:-----------------------------------------------------|
| Info                               | [beta] [gpio] [led] [electronics]                    |
| Description                        | Install led module (wiringPi)                        |
| Usage                              | /do/led/install                                      |
| Softwares                          | WiringPi, python-dev,                                |
| Variables                          | hardware=$(/pi/getBoard),                            |
| System                             | /system/installWiringPi, /system/install python-dev, |
| 1. [LED] Install                   |                                                      |
| 2. Install alternative to Rpi.GPIO |                                                      |

| /do/led/off                                     |                                                                                           |
|:------------------------------------------------|:------------------------------------------------------------------------------------------|
| Info                                            | [beta] [gpio] [led] [electronics] [orangepi]                                              |
| Description                                     | Turn off a led                                                                            |
| Usage                                           | /do/led/off pin                                                                           |
| Example                                         | /do/led/off 21                                                                            |
| Arguments                                       | 1:ledPin,                                                                                 |
| Variables                                       | hardware=$(/pi/getBoard), ledPin=$1, ledPin=$(/system/h3ToBcm $ledPin),                   |
| Modules                                         | /do/led/python/onoff_orange.py $ledPin 0 #Turn on led, /do/led/python/onoff.py $ledPin 0, |
| System                                          | ledPin=$(/system/h3ToBcm $ledPin),                                                        |
| 1. Turn off LED $ledPin                         |                                                                                           |
| 2. Could you tell me where the led is plugged ? |                                                                                           |

| /do/led/on                                      |                                                                                                        |
|:------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| Info                                            | [beta] [gpio] [led] [electronics] [orangepi]                                                           |
| Description                                     | Turn on a led                                                                                          |
| Usage                                           | /do/led/on pin                                                                                         |
| Example                                         | /do/led/on 21                                                                                          |
| Arguments                                       | 1:ledPin,                                                                                              |
| Variables                                       | hardware=$(/pi/getBoard), ledPin=$1, ledPin=$(/system/h3ToBcm $ledPin),                                |
| Modules                                         | /do/led/python/onoff_orange.py $ledPin 1 #Turn on led, /do/led/python/onoff.py $ledPin 1 #Turn on led, |
| System                                          | ledPin=$(/system/h3ToBcm $ledPin),                                                                     |
| 1. Turn on LED $ledPin  #Display text           |                                                                                                        |
| 2. Could you tell me where the led is plugged ? |                                                                                                        |

| /do/led/pulse                                          |                                                |
|:-------------------------------------------------------|:-----------------------------------------------|
| Info                                                   | [beta] [gpio] [led] [electronics] [orangepi]   |
| Description                                            | Software PWM with led                          |
| Usage                                                  | /do/led/pulse pin or /do/led/pulse pin speed   |
| Example                                                | /do/led/pulse 21 or /do/led/pulse 21 1         |
| Arguments                                              | 1:ledPin, 2:speed,                             |
| Variables                                              | hardware=$(/pi/getBoard), ledPin=$1, speed=$2, |
| Modules                                                | /do/led/python/pulse.py $ledPin $speed,        |
| 1. Could you tell me where the led is plugged ?        |                                                |
| 2. Sorry software PWM is not supported on an Orange Pi |                                                |
| 3. Pulse LED $ledPin                                   |                                                |

| /do/led/README.MD   |                        |
|:--------------------|:-----------------------|
| Info                | [alpha] [undocumented] |

| /do/led/state                                   |                                   |
|:------------------------------------------------|:----------------------------------|
| Info                                            | [beta] [gpio] [led] [electronics] |
| Description                                     | Check state of a led              |
| Usage                                           | /do/led/state pin                 |
| Example                                         | /do/led/state 21                  |
| System                                          | gpio read $(/system/bcmToWpi $1), |
| 1. Could you tell me where the led is plugged ? |                                   |

