import menu

import program1, program2, mbJehu, mbminecart, mbsurfacebrushing, mbMission6And7, crosssover

programs = {
    0: mbJehu.Run,
    1: mbminecart.Run,
    2: mbsurfacebrushing.Run,
    3: crosssover.Run,
    4: mbMission6And7.Run,
}

menu.menu(programs)
