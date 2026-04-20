import menu

import program1, program2, mbJehu, mbminecart, mbMapreveal, mbsurfacebrushing, mbMission6And7, crosssover, heavylifting, roofraising

programs = {
    0: mbJehu.Run,
    1: mbminecart.Run,
    2: mbMapreveal.Run,
    3: mbsurfacebrushing.Run,
    4: crosssover.Run,
    5: heavylifting.Run,
    6: mbMission6And7.Run,
    7: roofraising.Run,
}

menu.menu(programs)
