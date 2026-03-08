from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

import images

import mbMission6And7, mbMapreveal

TIRE_DIAMETER = 56  # mm - Large spike tires - 88 mm, small spike tires - 56 mm, projekt alpha tires 62.4 mm

AXLE_TRACK = (
    18 * 8
)  # distance between the wheels, mm - 16 studs * 8 mm each stud

print("Creating hub")
#hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.X)
hub = PrimeHub()

left_wheel = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(left_wheel, right_wheel, TIRE_DIAMETER, AXLE_TRACK)
left_attachment = Motor(Port.A, Direction.CLOCKWISE)
right_attachment = Motor(Port.B, Direction.CLOCKWISE)


#v = hub.battery.voltage()
#print("Battery voltage: " + str(v))

print("Hello")

programs = {
    0: mbMission6And7.Run,
    1: mbMapreveal.Run,
}

hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
hub.light.on(Color.BLUE)

selection = 0

while True:
    pressed = hub.buttons.pressed()
    if Button.RIGHT in pressed:
        selection += 1
        wait(200)
    if Button.LEFT in pressed:
        selection -= 1
        wait(200)
    if (selection < 0):
        selection = len(programs) - 1
    if selection > len(programs) - 1:
        selection = 0
    if Button.CENTER in pressed:
        hub.light.on(Color.MAGENTA)
        hub.display.animate(
            [
                images.RUNNING_1,
                images.RUNNING_2,
                images.RUNNING_3,
                images.RUNNING_4,
                images.RUNNING_5,
                images.RUNNING_6,
                images.RUNNING_7,
            ],
            300,
        )
        wait(500)
        hub.system.set_stop_button([Button.CENTER])
        try:
            programs[selection](drive_base, left_attachment, right_attachment)
        except SystemExit:
            drive_base.stop()
            left_attachment.stop()
            right_attachment.stop()
            wait(500)
            stopped = True
        hub.system.set_stop_button([Button.CENTER, Button.BLUETOOTH])
        selection += 1
        # if selection > len(programs) - 1 and not stopped:
        #     celebrate.Run(br)
    hub.display.number(selection)
    hub.light.on(Color.GREEN)
