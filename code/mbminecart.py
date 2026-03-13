from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
import robot


def Run(
    drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor
):
    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=500)
    drive_base.straight(765)
    drive_base.turn(90)
    drive_base.straight(380)
    drive_base.turn(-90)
    drive_base.straight(75)
    drive_base.straight(-50)
    left_attachment.run_angle(450, 180)
    drive_base.turn(-90)
    drive_base.straight(380)
    drive_base.turn(-90)
    drive_base.straight(780)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(robot.drive_base, robot.left_attachment, robot.right_attachment)
