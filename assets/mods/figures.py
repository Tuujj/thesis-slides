"""Static figures for the deck: loop diagrams (schemdraw) and matplotlib styling."""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import schemdraw
import schemdraw.elements
from schemdraw import dsp

schemdraw.use("matplotlib")  # text rendered as paths -> same font everywhere

INK = "#1f2328"
MUTED = "#8b949e"
ACCENT = "#d1495b"   # the "sound" / oscillation colour
LEARN = "#2e6fd8"    # learned components
MODEL_COLORS = {
    "True": INK,
    "NODE": "#e69f00",
    "PHNN": "#2e6fd8",
    "DHNN": "#009e73",
    "Linear": "#8b949e",
}


def style():
    plt.rcParams.update({
        "figure.dpi": 110,
        "font.size": 12,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": MUTED,
        "axes.labelcolor": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "axes.titlesize": 13,
        "axes.titleweight": "normal",
        "legend.frameon": False,
        "svg.fonttype": "path",
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
        "mathtext.fontset": "stixsans",
    })


def loop_diagram(learned: bool = False, feedback: bool = True, delay: bool = False) -> str:
    """Feedback loop: excitation -> (+) -> plant -> readout -> y, and back through
    DC blocker and gain g (no delay). With learned=True the plant is the neural model."""
    plant_label = "learned plant\n$f_\\vartheta(x) + G u$" if learned else "XY chain\n(rotors)"
    plant_color = LEARN if learned else INK
    ctrl_color = MUTED if learned else INK
    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=15, color=INK, lw=1.6)
        dsp.Arrow().right().length(2.4).label("excitation", loc="top")
        s = dsp.SumSigma()
        dsp.Arrow().right().at(s.E).length(2.2).label("$u$ (torque)", loc="top")
        p = dsp.Box(w=3.0, h=1.5).label(plant_label).anchor("W").color(plant_color)
        dsp.Arrow().right().at(p.E).length(1.3).label("$x$", loc="top")
        r = dsp.Box(w=2.6, h=1.9).label("readout\n$\\sin\\theta_{tap}$\n(or other)").anchor("W")
        dsp.Line().right().at(r.E).length(0.9)
        out = dsp.Dot()
        dsp.Arrow().right().at(out.center).length(1.2).label("$y$ (output)", loc="top").color(ACCENT)
        if not feedback:
            return responsive(d.get_imagedata("svg").decode())
        # return path: down, then left; the controller boxes are centred under the forward path
        gw, dcw, dw, gap = 1.9, 2.8, 2.2, 1.0
        chain = gw + gap + dcw + ((gap + dw) if delay else 0.0)
        mid = 0.5 * (s.S[0] + out.center[0])
        dsp.Line().down().at(out.center).length(2.4).color(ctrl_color)
        dsp.Arrow().left().length(out.center[0] - (mid + 0.5 * chain)).color(ctrl_color)
        g = dsp.Box(w=gw, h=1.0).label("gain $g$").anchor("E").color(ctrl_color)
        dsp.Arrow().left().at(g.W).length(gap).color(ctrl_color)
        dc = dsp.Box(w=dcw, h=1.0).label("DC block").anchor("E").color(ctrl_color)
        last = dc
        if delay:
            dsp.Arrow().left().at(dc.W).length(gap).color(ctrl_color)
            last = dsp.Box(w=dw, h=1.0).label("delay $d$").anchor("E").color(ctrl_color)
        dsp.Line().left().at(last.W).tox(s.S).color(ctrl_color)
        dsp.Arrow().up().toy(s.S).color(ctrl_color)
        if learned:
            schemdraw.elements.Label().at((0.5 * (g.center[0] + dc.center[0]), g.center[1] - 1.0)).label(
                "known controller (unchanged)", color=MUTED, fontsize=14)
    return responsive(d.get_imagedata("svg").decode())


def to_svg(fig) -> str:
    import io
    buf = io.StringIO()
    fig.savefig(buf, format="svg", bbox_inches="tight", transparent=True)
    plt.close(fig)
    return responsive(buf.getvalue())


def responsive(svg: str) -> str:
    """Drop fixed width/height so the SVG scales to its container (keeps viewBox)."""
    import re
    head, rest = svg.split("<svg", 1)
    tag, body = rest.split(">", 1)
    tag = re.sub(r'\s(width|height)="[^"]*"', "", tag)
    return f'{head}<svg{tag} style="width:100%;height:auto;display:block">{body}'

