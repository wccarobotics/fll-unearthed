import menu

import program1, program2, mbJehu, mbminecart, mbMapreveal, mbsurfacebrushing
import mbMission6And7, crosssover, heavylifting, roofraising, liftthedoor, mbJehuNew
import mbMinecartnew, mbwheelthing

programs = {
    0: mbMission6And7.Run,
    1: heavylifting.Run,
    2: liftthedoor.Run,
    3: mbwheelthing.Run,
    4: crosssover.Run,
    5: mbJehu.Run,
    6: mbMinecartnew.Run,
}

menu.menu(programs)
