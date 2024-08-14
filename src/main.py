from enum import StrEnum
from typing import Self, Optional

from enum import Enum

class Vowels(StrEnum):
    A = 'अ'
    AA = 'आ'
    I = 'इ'
    II = 'ई'
    U = 'उ'
    UU = 'ऊ'
    RI = 'ऋ'
    RII = 'ॠ'
    LI = 'ऌ'
    LII = 'ॡ'
    E = 'ए'
    AI = 'ऐ'
    O = 'ओ'
    AU = 'औ'

    def type(self):
        if self in [self.A, self.I, self.U, self.E, self.O]:
            return "laghu"


class Consonants(StrEnum):
    KA = 'क'
    KHA = 'ख'
    GA = 'ग'
    GHA = 'घ'
    NGA = 'ङ'
    CHA = 'च'
    CHHA = 'छ'
    JA = 'ज'
    JHA = 'झ'
    NYA = 'ञ'
    TA = 'ट'
    THA = 'ठ'
    DA = 'ड'
    DHA = 'ढ'
    NA = 'ण'
    TTA = 'त'
    TTHA = 'थ'
    DDA = 'द'
    DDHA = 'ध'
    NNA = 'न'
    PA = 'प'
    PHA = 'फ'
    BA = 'ब'
    BHA = 'भ'
    MA = 'म'
    YA = 'य'
    RA = 'र'
    LA = 'ल'
    VA = 'व'
    SHA = 'श'
    SSA = 'ष'
    SA = 'स'
    HA = 'ह'
    
class ConjuctConsonants(StrEnum):
    KSHA = 'क्ष'
    GNA = 'ज्ञ'
    TRA = 'त्र'
    
class Accents(StrEnum):
    UDATTA = '॑'
    ANUDATTA = '॒'
    SVARITA = '॒'

class Yogavaahas(StrEnum):
    ANUSVARA = 'ं'
    VISARGA = 'ः'
    
    # Additional symbols
    AVAGRAHA = 'ऽ'
    HALANT = '्'
    
class Digits(StrEnum):
    DIGIT_ZERO = '०'
    DIGIT_ONE = '१'
    DIGIT_TWO = '२'
    DIGIT_THREE = '३'
    DIGIT_FOUR = '४'
    DIGIT_FIVE = '५'
    DIGIT_SIX = '६'
    DIGIT_SEVEN = '७'
    DIGIT_EIGHT = '८'
    DIGIT_NINE = '९'

class Sabda():


# Example usage:
print(SanskritCharacters.A.name, SanskritCharacters.A.value)



class Matra:
    def __init__(self,chandas=None,svara=None, aksharas=None):
        self.chandas = chandas
        self.svara = svara
        self.aksharas = aksharas


m1 = Matra("Laghu",svara.UDATTA, aksharas=Consonants("na"))




class Padam:
    def __init__(self, text=None):
        self.text = text

    def __repr__(self):
        return f"Padam(text={self.text})"

    def __add__(self, other: Self) -> Self:
        pass

class Vaakyam:
    def __init__(self, padams: Optional[list[Padam]]):
        self.padams = padams
    
    def __insert__(self, padam):
        self.padams = self.padams.append(padam)


# representation of strings
# chandas
# swara


# add(p1,p2,..,pn)

# Padam("namas") + Padam("te")

def main():
    p1 = Padam("namah")
    p2 = Padam("te")
    p3 = Padam("rudra")
    p4 = Padam("manyave")
    p5 = Padam("uto iti")
    p6 = Padam("te")
    p7 = Padam("ishave")
    p8 = Padam("namah")

    print(p1)







if __name__ == "__main__":
    main()