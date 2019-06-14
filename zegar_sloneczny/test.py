import sys
import matplotlib
import logging as log
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import lines
from matplotlib import text
from collections import namedtuple

log.basicConfig(stream=sys.stdout, level=log.INFO)

# Lokalizacja
loc = namedtuple("loc", "latitude, longitude")

################################################################################
# Gliwice, Akademicka 14
LOC = loc(50.289204, 18.677464)  # Gliwice, Akademicka 14
HOUR_LINE_MIN = 5
HOUR_LINE_MAX = 20
# Great Pyramid of Giza
LOC = loc(29.979167, 31.134444)
HOUR_LINE_MIN = 6
HOUR_LINE_MAX = 18

# General
TZONE = 2
G_LENGTH = 0.9
N_OFFSET = 1.07
E_MAJOR = 1.15
E_MINOR = 0.7

################################################################################
def equ_hour_angle(hour, loc, tzone):
    equ_angle = (hour - tzone) * 2 * np.pi / 24 + (np.deg2rad(loc.longitude))

    log.getLogger("hour.angle.equ").debug(
        "For hour {0:d}, equatorial angle {1:g}".format(hour, np.rad2deg(equ_angle))
    )

    return equ_angle


################################################################################
def horiz_hour_angle(hour, loc, tzone):
    equ_angle = equ_hour_angle(hour, loc, tzone)
    equ_angle_from_solar_noon = equ_angle - np.pi

    log.getLogger("hour.angle.equ.noon").debug(
        "For hour {0:d}, equatorial angle from solar noon {1:g}".format(
            hour, equ_angle_from_solar_noon * 180 / np.pi
        )
    )

    a_x = np.cos(equ_angle_from_solar_noon)
    a_y = np.sin(equ_angle_from_solar_noon)

    horiz_angle_from_solar_noon = np.arctan2(
        a_y, a_x / np.sin(np.deg2rad(loc.latitude))
    )

    log.getLogger("hour.angle.horiz.noon").debug(
        "For hour {0:d}, horiz angle from solar noon {1:g}".format(
            hour, np.rad2deg(horiz_angle_from_solar_noon)
        )
    )

    return np.pi / 2 - horiz_angle_from_solar_noon


################################################################################
def main():
    fig = plt.figure()

    ax1 = fig.add_axes([0, 0, 1.0, 1.0], aspect="equal")

    hour_angle_logger = log.getLogger("hour.angle.horiz")

    for hour in range(HOUR_LINE_MIN, HOUR_LINE_MAX + 1):
        horiz_angle = horiz_hour_angle(hour, LOC, TZONE)
        if LOC.latitude < 0:
            horiz_angle += np.deg2rad(180)

        hour_angle_logger.info(
            "For hour {0:d}, horiz angle {1:g}".format(hour, np.rad2deg(horiz_angle))
        )

        line = lines.Line2D([0, np.cos(horiz_angle)], [0, np.sin(horiz_angle)])
        ax1.add_line(line)
        hour_text = "%d" % ((hour - 1) % 24 + 1)
        ax1.add_artist(
            text.Text(
                np.cos(horiz_angle) * N_OFFSET,
                np.sin(horiz_angle) * N_OFFSET,
                hour_text,
                ha="center",
                va="center",
            )
        )

    g_line = lines.Line2D([0, 0], [0, G_LENGTH], color="red")
    ax1.add_line(g_line)

    if LOC.latitude >= 0:
        ax1.add_artist(text.Text(0, -0.25, "N", ha="center", va="center"))
        arrow = matplotlib.patches.Arrow(0, -0.6, 0, 0.3, width=0.08, edgecolor="none")
        ax1.add_patch(arrow)
    else:
        ax1.add_artist(text.Text(0, -0.6, "N", ha="center", va="center"))
        arrow = matplotlib.patches.Arrow(
            0, -0.25, 0, -0.3, width=0.08, edgecolor="none"
        )
        ax1.add_patch(arrow)

    plt.axis("off")

    plt.xlim(-E_MAJOR, E_MAJOR)
    plt.ylim(-E_MINOR, E_MAJOR)

    plt.show()


################################################################################
if __name__ == "__main__":
    main()
