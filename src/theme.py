"""A theme for our plots"""
import vizta


def set():
    """Use the slide theme."""
    theme = vizta.mpl.MplTheme(
        palette="wfondrie",
        primary="#404040",
        accent="#01BCA3",
        rc_params={
            "font.family": "sans-serif",
            "font.sans-serif": ["Fira Sans"],
        },
    )

    return vizta.mpl.set_theme(context="talk", style=theme)
