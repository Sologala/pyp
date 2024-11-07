import argparse
import sys
from pyp import ffmpeg_group


all_entry = {"ffmpeg": ffmpeg_group.entry}


def main_entry():
    print(sys.argv)
    if sys.argv[1] in all_entry.keys():
        keyword = sys.argv[1]
        del sys.argv[1]
        all_entry[keyword]()
    else:
        print(all_entry.keys)
    # ffmpeg_group.entry()

