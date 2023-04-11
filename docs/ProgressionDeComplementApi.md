# osis_parcours_interne_sdk.ProgressionDeComplementApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/parcours_interne*

Method | HTTP request | Description
------------- | ------------- | -------------
[**progression_de_complement**](ProgressionDeComplementApi.md#progression_de_complement) | **GET** /{sigle_programme}/progression_de_complement/ | 


# **progression_de_complement**
> ProgressionDeComplement progression_de_complement(sigle_programme)



Return complement progress

### Example

* Api Key Authentication (Token):

```python
import time
import osis_parcours_interne_sdk
from osis_parcours_interne_sdk.api import progression_de_complement_api
from osis_parcours_interne_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_parcours_interne_sdk.model.error import Error
from osis_parcours_interne_sdk.model.progression_de_complement import ProgressionDeComplement
from pprint import pprint
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
    api_instance = progression_de_complement_api.ProgressionDeComplementApi(api_client)
    sigle_programme = "ECGE1BA" # str | The acronym of the offer
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.progression_de_complement(sigle_programme)
        pprint(api_response)
    except osis_parcours_interne_sdk.ApiException as e:
        print("Exception when calling ProgressionDeComplementApi->progression_de_complement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.progression_de_complement(sigle_programme, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_parcours_interne_sdk.ApiException as e:
        print("Exception when calling ProgressionDeComplementApi->progression_de_complement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sigle_programme** | **str**| The acronym of the offer |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**ProgressionDeComplement**](ProgressionDeComplement.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

