from dataclasses import dataclass
from cadquery import func as cf


@dataclass
class CellSpec:
    r_cell: float
    h_cell: float


def make_cell(spec):
    return cf.cylinder(d=2 * spec.r_cell, h=spec.h_cell)


def tray(spec, n=3, clearance=0.3, wall=4.0, thickness=6.0, depth=3.0,
         mounting_holes=True, hole_d=5.0):
    pocket_r = spec.r_cell + clearance
    pitch = 2 * pocket_r + wall

    length = n * pitch + wall
    width = 2 * pocket_r + 2 * wall

    plate = cf.box(length, width, thickness)
    pocket = cf.cylinder(d=2 * pocket_r, h=depth + 1).moved(z=thickness - depth)

    for i in range(n):
        x = (i - (n - 1) / 2) * pitch
        plate = plate - pocket.moved(x=x)

    # Upgrade: two mirrored mounting holes, drilled vertically through the plate.
    if mounting_holes:
        hole = cf.cylinder(d=hole_d, h=thickness + 1).moved(z=-0.5)
        hole_x = length / 2 - wall / 2
        plate = plate - hole.moved(x=-hole_x)
        plate = plate - hole.moved(x=hole_x)

    return plate


cells = {
    "18650": CellSpec(9.0, 65.0),
    "21700": CellSpec(10.5, 70.0),
    "4680": CellSpec(23.0, 80.0),
}


if __name__ == "__main__":
    for name, spec in cells.items():
        t = tray(spec)
        print(name, t.isValid(), round(t.Volume(), 1))
        t.exportStl(f"tray_{name}.stl")
