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
from osis_parcours_interne_sdk.model.barre_progression_bloc1 import BarreProgressionBloc1
from osis_parcours_interne_sdk.model.barre_progression_complement import BarreProgressionComplement
from osis_parcours_interne_sdk.model.barre_progression_cycle import BarreProgressionCycle
from osis_parcours_interne_sdk.model.complement import Complement
from osis_parcours_interne_sdk.model.credits_acquis_mini_formation import CreditsAcquisMiniFormation
from osis_parcours_interne_sdk.model.credits_progression_annuelle import CreditsProgressionAnnuelle
from osis_parcours_interne_sdk.model.cycle import Cycle
from osis_parcours_interne_sdk.model.error import Error
from osis_parcours_interne_sdk.model.hors_progression import HorsProgression
from osis_parcours_interne_sdk.model.mini_formation_cycle import MiniFormationCycle
from osis_parcours_interne_sdk.model.mobilite_cycle import MobiliteCycle
from osis_parcours_interne_sdk.model.partenariat_cycle import PartenariatCycle
from osis_parcours_interne_sdk.model.progression_de_cycle import ProgressionDeCycle
from osis_parcours_interne_sdk.model.tableau_de_progression import TableauDeProgression
from osis_parcours_interne_sdk.model.total_cycle import TotalCycle
from osis_parcours_interne_sdk.model.tronc_commun_cycle import TroncCommunCycle
