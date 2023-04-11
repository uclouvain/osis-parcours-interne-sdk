
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.progression_de_bloc_1_api import ProgressionDeBloc1Api
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from osis_parcours_interne_sdk.api.progression_de_bloc_1_api import ProgressionDeBloc1Api
from osis_parcours_interne_sdk.api.progression_de_complement_api import ProgressionDeComplementApi
from osis_parcours_interne_sdk.api.progression_de_cycle_api import ProgressionDeCycleApi
