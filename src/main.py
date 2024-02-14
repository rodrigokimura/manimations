from manim import (
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    WHITE,
    Create,
    CubicBezier,
    DrawBorderThenFill,
    Group,
    Line,
    Mobject,
    Polygon,
    Rectangle,
    Rotate,
    RoundedRectangle,
    Scene,
)

mm_to_unit = 1 / 19
UNIT = 0.6
SIZE = UNIT - 1 * mm_to_unit

BUFF = 0.1
ANIMATION_RUN_TIME = 0.5

N_ROWS = 5
N_COLS = 6

HORIZONTAL_GAP = 20.5


def create_switch():
    square = RoundedRectangle(width=SIZE, height=SIZE, corner_radius=0.1 * SIZE)
    square.set_style(stroke_width=2)
    square.set_fill(WHITE, opacity=0.4)
    return square


def create_outline(right=False):
    position_list: list[tuple[float, float, float]] = [
        (0.0, 0.0, 0.0),
        (19.0, 2.0, 0.0),
        (38.0, 17.0, 0.0),
        (38.0, 17.0, 0.0),
        (57.0, 22.0, 0.0),
        (80.0, 22.0, 0.0),
        (95.0, 16.0, 0.0),
        (114.0, 13.0, 0.0),
        (122.0, -2.0, 0.0),
        (140.0, -2.0, 0.0),
        (140.0, -64.0, 0.0),
        (160.0, -84.0, 0.0),
        (152.0, -104.0, 0.0),
        (132.419, -110.926, 0.0),
        (118.807, -97.418, 0.0),
        (102.451, -87.931, 0.0),
        (84.0, -83.0, 0.0),
        (46.0, -83.0, 0.0),
        (24.0, -81.0, 0.0),
        (0.0, -76.0, 0.0),
        (-7.0, -38.5, 0.0),
    ]
    position_list = [
        (
            x * mm_to_unit * UNIT * (1, -1)[right],
            y * mm_to_unit * UNIT,
            z * mm_to_unit * UNIT,
        )
        for x, y, z in position_list
    ]
    return Polygon(
        *position_list,
        color=WHITE,
        stroke_width=2,
        stroke_opacity=0.5,
    )


class Main(Scene):
    def construct(self):
        self.switches_l: list[list[Mobject]] = []
        self.switches_r: list[list[Mobject]] = []

        self.outline_l = create_outline(False)
        self.outline_r = create_outline(True)
        self.outline_l.shift(
            (3 + 0.5) * UNIT * UP,
            (22 * mm_to_unit) * UNIT * DOWN,
            (HORIZONTAL_GAP / 2 + 0.5) * UNIT * LEFT,
        )
        self.outline_r.shift(
            (3 + 0.5) * UNIT * UP,
            (22 * mm_to_unit) * UNIT * DOWN,
            (HORIZONTAL_GAP / 2 + 0.5) * UNIT * RIGHT,
        )

        trrs_l = Rectangle(height=8 * mm_to_unit * UNIT, width=4 * mm_to_unit * UNIT)
        trrs_l.set_style(stroke_width=2, stroke_opacity=0.5)
        trrs_r = Rectangle(
            height=8 * mm_to_unit * UNIT, width=4 * mm_to_unit * UNIT
        ).flip()
        trrs_r.set_style(stroke_width=2, stroke_opacity=0.5)
        trrs_l.shift(
            (3 + 0.5) * UNIT * UP,
            (22 * mm_to_unit) * UNIT * DOWN,
            (HORIZONTAL_GAP / 2 + 0.5) * UNIT * LEFT,
            (106 * mm_to_unit + 2) * UNIT * RIGHT,
            72 * mm_to_unit * UNIT * DOWN,
        )
        trrs_l.rotate(-PI / 4 - PI / 24)
        trrs_r.shift(
            (3 + 0.5) * UNIT * UP,
            (22 * mm_to_unit) * UNIT * DOWN,
            (HORIZONTAL_GAP / 2 + 0.5) * UNIT * RIGHT,
            (106 * mm_to_unit + 2) * UNIT * LEFT,
            72 * mm_to_unit * UNIT * DOWN,
        )
        trrs_r.rotate(PI / 4 + PI / 24)
        cable_seg_l = CubicBezier(
            start_anchor=25 * mm_to_unit * UNIT * DOWN + 57 * mm_to_unit * UNIT * LEFT,
            start_handle=45 * mm_to_unit * UNIT * LEFT + 15 * mm_to_unit * UNIT * DOWN,
            end_handle=45 * mm_to_unit * UNIT * LEFT + 15 * mm_to_unit * UNIT * DOWN,
            end_anchor=30 * mm_to_unit * UNIT * UP + 45 * mm_to_unit * UNIT * LEFT,
            stroke_width=2,
            stroke_opacity=0.5,
        )
        cable_seg_r = CubicBezier(
            start_anchor=30 * mm_to_unit * UNIT * UP + 45 * mm_to_unit * UNIT * RIGHT,
            start_handle=45 * mm_to_unit * UNIT * RIGHT + 15 * mm_to_unit * UNIT * DOWN,
            end_handle=45 * mm_to_unit * UNIT * RIGHT + 15 * mm_to_unit * UNIT * DOWN,
            end_anchor=25 * mm_to_unit * UNIT * DOWN + 57 * mm_to_unit * UNIT * RIGHT,
            stroke_width=2,
            stroke_opacity=0.5,
        )
        spiral = [
            Line(
                start=30 * mm_to_unit * UNIT * UP
                + 45 * mm_to_unit * UNIT * LEFT
                + (3 * i) * mm_to_unit * UNIT * RIGHT,
                end=20 * mm_to_unit * UNIT * UP
                + 45 * mm_to_unit * UNIT * LEFT
                + (3 * i) * mm_to_unit * UNIT * RIGHT,
                stroke_width=2,
                stroke_opacity=0.5,
            )
            for i in range(1, 30)
        ]

        for row_idx in range(N_ROWS):
            row_l: list[Mobject] = [create_switch() for _ in range(N_COLS)]

            self.switches_l.append(row_l)

            row_r: list[Mobject] = [create_switch() for _ in range(N_COLS)]
            self.switches_r.append(row_r)

            for col_idx, s in enumerate(row_l):
                s.shift(
                    3 * UNIT * UP,
                    5.5 * UNIT * LEFT,
                    row_idx * UNIT * DOWN,
                    col_idx * UNIT * RIGHT,
                )

            for col_idx, s in enumerate(row_r):
                s.shift(
                    3 * UNIT * UP,
                    5.5 * UNIT * RIGHT,
                    row_idx * UNIT * DOWN,
                    col_idx * UNIT * LEFT,
                )

            for sl, sr in zip(row_l, row_r):
                self.play(
                    DrawBorderThenFill(sl),
                    DrawBorderThenFill(sr),
                    run_time=(ANIMATION_RUN_TIME / 5),
                )

        self.play(
            *(
                s.animate.shift((HORIZONTAL_GAP / 2 - 5.5) * UNIT * LEFT)
                for r in self.switches_l
                for s in r
            ),
            *(
                s.animate.shift((HORIZONTAL_GAP / 2 - 5.5) * UNIT * RIGHT)
                for r in self.switches_r
                for s in r
            ),
            run_time=ANIMATION_RUN_TIME,
        )

        thumb_cluster_l: list[Mobject] = []
        thumb_cluster_r: list[Mobject] = []
        for col_idx in range(N_COLS):
            thumb_cluster_l.append(self.switches_l[-1][col_idx])
            thumb_cluster_r.append(self.switches_r[-1][col_idx])

        positions = [
            (46, 9.95),
            (46, 9.95),
            (46 + 2.191, 9.95 + 2.79),
            (46 + 2.191 + 0.747, 9.95 + 2.79 + 8.179),
            (46 + 2.191 + 0.747 - 2.043, 9.95 + 2.79 + 8.179 + 13.011),
            (
                46 + 2.191 + 0.747 - 2.043 - 5.565,
                9.95 + 2.79 + 8.179 + 13.011 - 13.435,
            ),
        ]

        angles = (0, 0, -PI / 12, -PI / 12 * 2, -PI / 12 * 3, -PI / 12 * 3)

        self.play(
            *(Rotate(s, a) for s, a in zip(thumb_cluster_l, angles)),
            *(Rotate(s, -a) for s, a in zip(thumb_cluster_r, angles)),
            run_time=ANIMATION_RUN_TIME,
        )

        animations = []
        for p, sl, sr in zip(positions, thumb_cluster_l, thumb_cluster_r):
            x, y = p
            animations.append(
                sl.animate.shift(
                    x * mm_to_unit * UNIT * RIGHT,
                    y * mm_to_unit * UNIT * DOWN,
                )
            )
            animations.append(
                sr.animate.shift(
                    x * mm_to_unit * UNIT * LEFT,
                    y * mm_to_unit * UNIT * DOWN,
                )
            )
        self.play(*animations, run_time=ANIMATION_RUN_TIME)

        col_offsets = [22, 20, 5, 0, 6, 9]
        for col_idx, o in enumerate(col_offsets):
            switches_l: list[Mobject] = []
            switches_r: list[Mobject] = []
            for r in range(N_ROWS - 1):
                switches_l.append(self.switches_l[r][col_idx])
                switches_r.append(self.switches_r[r][col_idx])

            if o:
                self.play(
                    *(
                        s.animate.shift(o * mm_to_unit * UNIT * DOWN)
                        for s in switches_l
                    ),
                    *(
                        s.animate.shift(o * mm_to_unit * UNIT * DOWN)
                        for s in switches_r
                    ),
                    run_time=ANIMATION_RUN_TIME,
                )
        self.play(Create(self.outline_l), Create(self.outline_r), run_time=0.5)

        left_side = Group(*(s for r in self.switches_l for s in r), self.outline_l)
        right_side = Group(*(s for r in self.switches_r for s in r), self.outline_r)

        self.play(
            left_side.animate.rotate(-PI / 24),
            right_side.animate.rotate(PI / 24),
            run_time=ANIMATION_RUN_TIME,
        )

        self.play(Create(trrs_l), run_time=ANIMATION_RUN_TIME)
        self.play(Create(cable_seg_l), run_time=ANIMATION_RUN_TIME)
        for s in spiral:
            self.play(Create(s), run_time=(ANIMATION_RUN_TIME / len(spiral)))
        self.play(Create(cable_seg_r), run_time=ANIMATION_RUN_TIME)
        self.play(Create(trrs_r), run_time=ANIMATION_RUN_TIME)

        self.wait(10)
