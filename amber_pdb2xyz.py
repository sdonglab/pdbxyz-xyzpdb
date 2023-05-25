import os
import argparse
from typing import Optional, List

__doc__ = """
1. Read AMBER prm file
    - `grep "^atom" amber_prm_file > tmp_atom_lines`
2. 
"""

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--amber_prm", type=str, required=True, help="the path to the AMBER parameter file")
    parser.add_argument("input_pdb", type=str, help="the path to the input PDB file to convert")
    parser.add_argument("output_xyz", type=str, help="the path to the output XYZ file")

    return parser

def process_opts(parser: argparse.ArgumentParser, opts: argparse.Namespace):
    input_files = [opts.amber_prm, opts.input_pdb]
    for path in input_files:
        if not os.path.exists(path):
            parser.error(f"{path} does not exist")

def main(args: Optional[List[str]] = None):
    parser = get_parser()
    opts = parser.parse_args(args)
    process_opts(parser, opts)

    print(opts)

if __name__ == '__main__':
    main()
