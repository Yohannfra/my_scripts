#!/usr/bin/env python3

# This scripts converts a .svg file to a .png using inkscape cli

import sys
import argparse
import os

def main():
    parser = argparse.ArgumentParser(
        prog='svg_to_png', description='Convert a svg file to a png', add_help=False)
    parser.add_argument('-w', '--width')
    parser.add_argument('-h', '--height')
    parser.add_argument('svg_file')
    args = parser.parse_args()

    if sys.platform == 'darwin':
        inkscape_cli_path = "/Applications/Inkscape.app/Contents/MacOS/inkscape"
    else:
        inkscape_cli_path = "inkscape"

    (file_name, _) = os.path.splitext(args.svg_file)
    png_file_name = file_name + '.png'

    os.system(
        f'{inkscape_cli_path} -w {args.width} -h {args.height} {args.svg_file} -o {png_file_name}')


if __name__ == '__main__':
    main()
