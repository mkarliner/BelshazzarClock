# Belshazzar Luminous Night Clock


Here are the files for the PCB, micropython code and STL files for Belshazzar's Clock.
Refer to the KiCad files for the PCB details and BOM for details of compononents, but they
are basically WS2811 SOT8 led drivers, 0805 SMD UV leds and a a small number of resistors and
caps, also 0805 SMD.

There are four 3D printed parts, which are small enough to print on most printers.

You will additionally need -

- Stepper Motor 28BYJ-48 with ULN2003 Driver Board
- 200mm of 100mm ID plastic ducting pipe.
- White paint or paper to cover the pipe
- Glow in the dark paint
- ESP32C3 Super Mini dev board

  I've left a space for a 74AHCT125 level converter to boost the 3.3V logic of the ESP32 to 5V for the WS2811, but on my board at least, it works fine without, you can just jumper over the in and out pins on the level converter. 
