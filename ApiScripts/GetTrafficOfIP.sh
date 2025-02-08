#!/bin/bash

echo "Getting Traffic Data from $1"

default_zone="$2"

if [[ "$3" == "L" ]]; then
	fil=', "securityAction": "unknown"'
else
	fil=''
fi

echo '{ "query":
  "{
    viewer {
      zones(filter: { zoneTag: $zoneTag }) {
      httpRequestsAdaptive(
          filter: $filter
          limit: 10000
          orderBy: [datetime_DESC]
        ) {
            datetime
            cacheStatus
            clientASNDescription
            clientAsn
            clientCountryName
            clientDeviceType
            clientIP
            clientRequestHTTPHost
            clientRequestHTTPMethodName
            clientRequestHTTPProtocol
            clientRequestPath
            clientRequestQuery
            clientRequestScheme
            clientSSLProtocol
            edgeResponseStatus
            leakedCredentialCheckResult
            originResponseDurationMs
            requestSource
            securityAction
            securitySource
            userAgent
            clientRequestReferer
            clientRefererHost
            xRequestedWith
            originIP
            originASN
            originResponseStatus
        }
      }
    }
  }",
  "variables": {
    "zoneTag": "'"$default_zone"'",
    "filter": {
       "datetime_geq": "'"$5"'",
       "datetime_leq": "'"$6"'",
       "clientIP": "'"$1"'"
       '"$fil"'
     }
  }
}' | tr -d '\n' | curl --silent -4 \
https://api.cloudflare.com/client/v4/graphql \
--header "Authorization: Bearer $4" \
--header "Content-Type: application/json" \
--data @- > "logs/log_$7_$6.json"

entries="$(grep -o 'userAgent' logs/log_$7_$6.json | wc -l)"

if [ "$entries" = "1000" ]; then
       	echo "Number of entries exceeds limit for $1"
fi

if [ "$entries" = "0" ]; then
       	echo "Failed to receive any entries for $1"
fi

echo "Received log file for $1 with $entries entries - saved to logs/log_$7_$6.json"

exit 0

