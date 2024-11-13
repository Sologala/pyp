import argparse
from re import A
import sys
import fire
from pyp import ffmpeg_group


app = {"ffmpeg": ffmpeg_group.app}


def main_entry() -> None:
    fire.Fire(app)
