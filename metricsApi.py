"""
List tags by metric name returns "Success" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi

# there is a valid "metric_tag_configuration" in the system
# METRIC_TAG_CONFIGURATION_DATA_ID = environ["datadog.agent.python.version"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.list_tags_by_metric_name(
        metric_name="zstallTester.metric"
    )

    print(response)



    '''
    # Path parameters
export metric_name="dist.http.endpoint.request"
# Curl command
curl -X GET "https://api.datadoghq.com/api/v2/metrics/zstallTester.metric/all-tags" \
-H "Accept: application/json" \
-H "DD-API-KEY: <PUT KEY HERE>" \
-H "DD-APPLICATION-KEY: <PUT APP KEY HERE>"
'''


# Curl command
curl -X POST "https://api.datadoghq.com/api/v2/metrics/config/bulk-tags" \
-H "Accept: application/json" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: <PUT KEY HERE>" \
-H "DD-APPLICATION-KEY: <PUT KEY HERE" \
-d @- << EOF
{
  "data": {
    "attributes": {
      "emails": [
        "zachary.stall@datadoghq.com"
      ],
      "tags": [
        "test",
        "tester",
        "addingAllTheTags"
      ]
    },
    "id": "zstallTester",
    "type": "metric_bulk_configure_tags"
  }
}
EOF
