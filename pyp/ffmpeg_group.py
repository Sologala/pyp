import ffmpeg
import argparse
import sys

def concat():
    print(sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inp", '-i', help="input video path",  required=True, nargs='+')
    parser.add_argument(
        "--out", '-o', help="out video path",  required=True)
    
    args = parser.parse_args()
    inpvideos = args.inp
    print(args.inp)
    print(args.out)
    # ins = [ffmpeg.input(inp) for inp in inpvideos]

    ffmpeg.filter(*inpvideos, 'hstack', 'inputs=' +
                  str(len(inpvideos))).output(args.out).run()
    pass


all_entry = {"concat": concat}

def entry():
    if sys.argv[1] in all_entry.keys():
        keyword = sys.argv[1]
        del sys.argv[1]
        all_entry[keyword]()
    else:
        print(all_entry.keys)
    

