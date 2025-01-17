from manimlib import *


def m_line(x,
           y,
           z=None,
           axes=None,
           color=None,
           width=None,
           optacity=None,
           background=None):
    """point data to line"""
    L = len(x)
    x, y = np.array(x), np.array(y)
    if z is None:
        z = np.zeros(x.shape)
    if axes is None:
        # last_little_line = Line([x[L - 1], y[L - 1], z[0]], [x[0], y[0], z[0]])
        line = VGroup(*[
            Line([x[i], y[i], 0], [x[i + 1], y[i + 1]]).set_stroke(
                color=color,
                width=width,
                opacity=optacity,
                background=background) for i in range(len(x) - 1)
        ])
    elif type(axes) is Axes:
        # last_little_line = Line(axes.c2p(x[L - 1], y[L - 1]),
        #                         axes.c2p(x[0], y[0]))
        line = VGroup(*[
            Line(axes.c2p(x[i], y[i]), axes.c2p(x[i + 1], y[
                i + 1])).set_stroke(color=color,
                                    width=width,
                                    opacity=optacity,
                                    background=background)
            for i in range(len(x) - 1)
        ])
    else:  # ThreeDAxes
        # last_little_line = Line(axes.c2p(x[L - 1], y[L - 1], z[0]),
        #                         axes.c2p(x[0], y[0], z[0])).set_stroke(
        #     color=color, width=width, opacity=optacity, background=background)

        line = VGroup(*[
            Line(axes.c2p(x[i], y[i], z[i]), axes.c2p(x[i + 1], y[
                i + 1], z[i])).set_stroke(color=color,
                                          width=width,
                                          opacity=optacity,
                                          background=background)
            for i in range(len(x) - 1)
        ])
    return line


def m_scatter(x, y, z=None, axes=None):
    """for scatter plot"""
    x, y = np.array(x), np.array(y)
    if z is None:
        z = np.zeros(x.shape)
    dots = VGroup(
        *
        [Dot(radius=.01).move_to([xi, yi, zi]) for xi, yi, zi in zip(x, y, z)])

    return dots
