| /do/led/blink   |                                                               |
|:----------------|:--------------------------------------------------------------|
| Description     | Blink a led                                                   |
| Example         | /do/led/blink 21 or /do/led/blink 21 3 /do/led/blink 21 3 0.1 |
| Info            | [beta] [gpio] [led] [electronics]                             |
| Arguments       | 1:ledPin, 2:loopUntil, 2:loopUntil, 3:speed,                  |

| /do/led/install   |                                   |
|:------------------|:----------------------------------|
| Description       | Install led module (wiringPi)     |
| Info              | [beta] [gpio] [led] [electronics] |

| /do/led/off   |                                   |
|:--------------|:----------------------------------|
| Description   | Turn off a led                    |
| Example       | /do/led/off 21                    |
| Info          | [beta] [gpio] [led] [electronics] |
| Arguments     | 1:ledPin,                         |

| /do/led/on   |                                   |
|:-------------|:----------------------------------|
| Description  | Turn off a led                    |
| Example      | /do/led/on 21                     |
| Info         | [beta] [gpio] [led] [electronics] |
| Arguments    | 1:ledPin,                         |

| /do/led/pulse   |                                        |
|:----------------|:---------------------------------------|
| Description     | Software PWM with led                  |
| Example         | /do/led/pulse 21 or /do/led/pulse 21 1 |
| Info            | [beta] [gpio] [led] [electronics]      |
| Arguments       | 1:ledPin, 2:speed,                     |

| /do/led/state   |                                   |
|:----------------|:----------------------------------|
| Description     | Check state of a led              |
| Example         | /do/led/state 21                  |
| Info            | [beta] [gpio] [led] [electronics] |

