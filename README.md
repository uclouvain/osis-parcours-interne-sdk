# osis-parcours-interne-sdk
A set of API endpoints that gives you information about your internal path and progress

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.02
- Package version: 1.02
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import osis_parcours_interne_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import osis_parcours_interne_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import osis_parcours_interne_sdk
from pprint import pprint
from osis_parcours_interne_sdk.api import progression_api
from osis_parcours_interne_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_interne_sdk.model.error import Error
from osis_parcours_interne_sdk.model.progression_de_bloc1 import ProgressionDeBloc1
from osis_parcours_interne_sdk.model.progression_de_complement import ProgressionDeComplement
from osis_parcours_interne_sdk.model.progression_de_cycle import ProgressionDeCycle
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/parcours_interne
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_parcours_interne_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/parcours_interne"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'


# Enter a context with an instance of the API client
with osis_parcours_interne_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = progression_api.ProgressionApi(api_client)
    sigle_programme = "ECGE1BA" # str | The acronym of the offer
accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
x_user_first_name = "X-User-FirstName_example" # str |  (optional)
x_user_last_name = "X-User-LastName_example" # str |  (optional)
x_user_email = "X-User-Email_example" # str |  (optional)
x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    try:
        api_response = api_instance.get_progression_de_bloc1(sigle_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_interne_sdk.ApiException as e:
        print("Exception when calling ProgressionApi->get_progression_de_bloc1: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/parcours_interne*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ProgressionApi* | [**get_progression_de_bloc1**](docs/ProgressionApi.md#get_progression_de_bloc1) | **GET** /{sigle_programme}/progression_de_bloc_1/ | 
*ProgressionApi* | [**get_progression_de_complement**](docs/ProgressionApi.md#get_progression_de_complement) | **GET** /{sigle_programme}/progression_de_complement/ | 
*ProgressionApi* | [**get_progression_de_cycle**](docs/ProgressionApi.md#get_progression_de_cycle) | **GET** /{sigle_programme}/progression_de_cycle/ | 


## Documentation For Models

 - [AcceptedLanguageEnum](docs/AcceptedLanguageEnum.md)
 - [Error](docs/Error.md)
 - [ProgressionDeBloc1](docs/ProgressionDeBloc1.md)
 - [ProgressionDeComplement](docs/ProgressionDeComplement.md)
 - [ProgressionDeCycle](docs/ProgressionDeCycle.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in osis_parcours_interne_sdk.apis and osis_parcours_interne_sdk.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from osis_parcours_interne_sdk.api.default_api import DefaultApi`
- `from osis_parcours_interne_sdk.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import osis_parcours_interne_sdk
from osis_parcours_interne_sdk.apis import *
from osis_parcours_interne_sdk.models import *
```

