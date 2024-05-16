# test_utils.py
import pytest
from utils.utils import *

@pytest.fixture
def dataset():
    return {
  89345: 'quatre-vingt-neuf-mille-trois-cent-quarante-cinq',
  618128: 'six-cent-dix-huit-mille-cent-vingt-huit',
  573334: 'cinq-cent-soixante-treize-mille-trois-cent-trente-quatre',
  39204: 'trente-neuf-mille-deux-cent-quatre',
  446695: 'quatre-cent-quarante-six-mille-six-cent-quatre-vingt-quinze',
  899384: 'huit-cent-quatre-vingt-dix-neuf-mille-trois-cent-quatre-vingt-quatre',
  575879: 'cinq-cent-soixante-quinze-mille-huit-cent-soixante-dix-neuf',
  705024: 'sept-cent-cinq-mille-vingt-quatre',
  168097: 'cent-soixante-huit-mille-quatre-vingt-dix-sept',
  141951: 'cent-quarante-et-un-mille-neuf-cent-cinquante-et-un',
  219524: 'deux-cent-dix-neuf-mille-cinq-cent-vingt-quatre',
  603841: 'six-cent-trois-mille-huit-cent-quarante-et-un',
  128485: 'cent-vingt-huit-mille-quatre-cent-quatre-vingt-cinq',
  481625: 'quatre-cent-quatre-vingt-un-mille-six-cent-vingt-cinq',
  153562: 'cent-cinquante-trois-mille-cinq-cent-soixante-deux',
  984910: 'neuf-cent-quatre-vingt-quatre-mille-neuf-cent-dix',
  216178: 'deux-cent-seize-mille-cent-soixante-dix-huit',
  193283: 'cent-quatre-vingt-treize-mille-deux-cent-quatre-vingt-trois',
  295086: 'deux-cent-quatre-vingt-quinze-mille-quatre-vingt-six',
  854372: 'huit-cent-cinquante-quatre-mille-trois-cent-soixante-douze'
}


def test_number_to_french(dataset):
    for k, v in dataset.items():
        assert number_to_french(k) == v