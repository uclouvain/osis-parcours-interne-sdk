# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_parcours_interne_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_parcours_interne_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_interne_sdk.model.credits_acquis_mini_formation import CreditsAcquisMiniFormation
from osis_parcours_interne_sdk.model.error import Error
from osis_parcours_interne_sdk.model.progression_de_bloc1 import ProgressionDeBloc1
from osis_parcours_interne_sdk.model.progression_de_complement import ProgressionDeComplement
from osis_parcours_interne_sdk.model.progression_de_cycle import ProgressionDeCycle
