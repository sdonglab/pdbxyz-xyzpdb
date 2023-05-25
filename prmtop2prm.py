"""
Convert an AMBER prmtop force field parameter file to a TINKER prm
"""

import argparse
from typing import Optional, List, Union

import parmed as pmd
from parmed import amber
from functools import cached_property


TINKER_COMMENT_CHAR = '#'
X_AMBER_ATOM_TYPE = 'X'
X_TINKER_ATOM_TYPE = '999'



def make_tinker_header(info: Union[str, List[str]],
                       left_pad: int = 6,
                       horiz_border_thickness: int = 2,
                       vert_border_thickness: int = 1,
                       horiz_title_pad: int = 2,
                       vert_title_pad: int = 1):
    """
    Create a string that mimics the TINKER section headers found in the prm
    files. For example

            ##############################
            ##                          ##
            ##  Force Field Definition  ##
            ##                          ##
            ##############################
    
    :param info: The information to place into the header in the form of a
        single string or a list of string representing multiple lines to
        display. In either form new line characters are not permitted in the
        strings. To display multiple lines of information provide each line
        as an element in a list of strings.
    :param left_pad: How many leading spaces to include for each row in the
        header
    :param horiz_title_pad: How many spaces to place on the left and right
        side of the title
    :param vert_title_pad: How many spaces to place above and below the title
    :param horiz_border_thickness: How many comment characters wide the
        horizontal border should be
    :param vert_border_thickness: How many comment characters tall the vertical
        border should be
    """
    info_lines = [info] if type(info) is str else info
    for line in info_lines:
        if '\n' in line:
            raise ValueError('info lines may not contain new line characters')

    longest_line = max(len(line) for line in info_lines)
    inner_rect_len = longest_line + (2 * horiz_title_pad)
    outer_rect_len = inner_rect_len + (2 * horiz_border_thickness)

    top_border = TINKER_COMMENT_CHAR * outer_rect_len
    horiz_wall = TINKER_COMMENT_CHAR * horiz_border_thickness

    top_borders = [top_border for _ in range(vert_border_thickness)]
    empty_lines = ['' for _ in range(vert_title_pad)]
    info_lines = [*empty_lines, *info_lines, *empty_lines]
    info_rows = [
        f'{horiz_wall}{line.center(inner_rect_len)}{horiz_wall}'
        for line in info_lines
    ]

    rows = [*top_borders, *info_rows, *top_borders]
    left_pad_str = ' ' * left_pad
    padded_rows = [left_pad_str + row for row in rows]
    return '\n'.join(padded_rows)


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('input_prmtop')
    parser.add_argument('output_prm')
    return parser


class AmberToTinkerConvertor:

    
    def __init__(self, amber_prmtop_path: str):
        self._amber_parm = pmd.load_file(amber_prmtop_path)
        self._amber_param_set = amber.AmberParameterSet.from_structure(self._amber_parm)

    @cached_property
    def amber_to_tinker_at(self):
        mapping = {X_AMBER_ATOM_TYPE: X_TINKER_ATOM_TYPE}
        for i, amber_at in enumerate(self._amber_param_set.atom_types, 1):
            mapping[amber_at] = i
        
        return mapping
    
    def amber_rmin14(self, amber_at):
        return self._amber_param_set[amber_at].rmin_14
    
    def amber_eps14(self, amber_at):
        return self._amber_param_set[amber_at].epsilon_14

    def convert(self, tinker_prm_path: str, ff_name: str = 'AMBER'):
        pass


def main(args: Optional[List[str]] = None):
    parser = get_parser()
    opts = parser.parse_args()

    convertor = AmberToTinkerConvertor(opts.input_prmtop)
    convertor.convert(opts.output_prm)
