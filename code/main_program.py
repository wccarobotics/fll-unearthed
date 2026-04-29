from marcus.menu import menu

import mbJehu, mbminecart, mbMapreveal, mbsurfacebrushing
import mbMission6And7, crosssover, heavylifting, roofraising, liftthedoor, mbJehuNew
import mbMinecartnew, mbwheelthing

programs = [
    mbMission6And7.Run,
    heavylifting.Run,
    mbwheelthing.Run,
    liftthedoor.Run,
    mbJehuNew.Run,
    mbMinecartnew.Run,
]

menu(programs)

print("done")
