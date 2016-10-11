Basic led control using simple commands.   
GPIO is manage using python scripts

|Author                 |Rémi Sarrailh                       |
|:---------------------:|:----------------------------------:|
|License                | MIT                                |

# Prequisite
[piget-core](https://github.com/pigetnet/core)

# Install
Type this command in your terminal
````
/pi/install led
````

# Control Act led

By default, the green led (ACT led) light up when data is read or write on the SD card.
Here is how to control it :

* Turn on LED: /pi/ledOn
* Turn off LED: /pi/ledOff
* Blink LED: /pi/ledBlink
* Return LED to normal state: /pi/ledReset

# Control a led on GPIO

## Wiring
Here is how to plug a led on GPIO 21
![Pinout](https://raw.githubusercontent.com/pigetnet/led/master/doc/schema_led.png)

* Wire the LED + (the longest leg) on pin 21
* Wire the LED  - on a (at least 100 ohms) resistor
* Wire the resistor to the ground, next to pin 21.

If you want to plug a led on another pin, there is a list on http://pinout.xyz

## How to find the right resistor
You can find which resistor you need for your led on : http://led.linear1.org/1led.wiz
![Resistor](https://raw.githubusercontent.com/pigetnet/led/master/doc/resistor.png)

## Commands
Here is a list of commands
* Turn on LED: /do/led/on 21
* Turn off LED: /do/led/off 21
* Blink LED: /do/led/blink 21
* Change led intensity: /do/led/pulse 21
* Display state of led (0:off 1:on): /do/led/state 21
* Display gpio: /show/gpio

## Advanced commands
You can use additional arguments on some commands.
/do/led/blink
````
/do/led/blink   pin    number_of_blink
/do/led/blink 21 5

/do/led/blink   pin    number_of_blink    speed (in seconds)
/do/led/blink 21 5 0.05
````

/do/led/pulse
```
/do/led/pulse   pin    speed
/do/led/pulse 21 0.3
```
