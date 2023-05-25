from dataclasses import dataclass

from typing import List

class TinkerKey:

    KEYWORD = None
    KEYWORD_WIDTH = 12

    def format(self) -> str:
        raise NotImplementedError
    
    def __str__(self) -> str:
        return f'{self.KEYWORD:self.KEYWORD_WIDTH}{self.format()}'


@dataclass
class Atom(TinkerKey):
    KEYWORD = 'atom'

    type: int
    cls: int
    name: str
    description: str
    atomic_number: int
    atomic_mass: float
    valence: int

    def format(self) -> str:
        return (
            f'{self.type:4}'
        )
        # "atom       {:4}  {:2}    {:<4}  \"{:<30} {:3}   {:>7.2f}    {}\n".format((i+1),\
        # return f'{self.type:4}{self.cls:-3}'
    
    

@dataclass
class VDW:
    atom_class: int
    size: float
    well_depth: float
    reduction_factor: float

@dataclass
class Bond:
    atom_class1: int
    atom_class2: int
    k: float
    ideal_length: float

@dataclass
class Angle:
    atom_class1: int
    atom_class2: int
    atom_class3: int
    k: float
    ideal_angles: List[float]

@dataclass
class ImproperTors:
    pass

@dataclass
class Tors:
    pass

@dataclass
class Charge:
    pass


@dataclass
class TinkerPRM:
    atoms: List[Angle]
    vdws: List[VDW]
    bonds: List[Bond]
    angles: List[Angle]
    imptors: List[ImproperTors]
    tors: List[Tors]
    charges: List[Charge]
