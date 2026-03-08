from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

def Run(drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor):
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(695)
    drive_base.turn(-45)
    drive_base.straight(300)
    drive_base.straight(-300)
    drive_base.turn(75)
    drive_base.straight(-735)
