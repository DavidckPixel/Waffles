#!/bin/bash
# This BASH script will get all blocked network traffic from a cloudflair WAF
# Between a certain time-limit (max 72 hours)
#
# Param1: is a zone_id
# Param2: start-date, format: yyyy-mm-ddThh-mm-ssZ
# Param3: end-date, format: yyyy-mm-ddThh-mm-ssZ
# Param4: Cloudflare API key, DO NOT SHARE
#
# output is saved in logs folder

echo "Getting Blocked Network Traffic from $2 till $3 for $5"

default_zone='$1'

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
    "zoneTag": "'"$1"'",
    "filter": {
      "datetime_geq": "'"$2"'",
      "datetime_leq": "'"$3"'",
      "securityAction_neq": "unknown"
    }
  }
}' | tr -d '\n' | curl --silent -4 \
https://api.cloudflare.com/client/v4/graphql \
--header "Authorization: Bearer $4" \
--header "Content-Type: application/json" \
--data @- > "logs/log_blocked_$5_$2_$3.json"

entries="$(grep -o 'userAgent' logs/log_blocked_$5_$2_$3.json | wc -l)"

if [ "$entries" = "1000" ]; then
       	echo "Number of blocked entries exceeds limit for $2 till $3"
fi

if [ "$entries" = "0" ]; then
       	echo "Failed to receive any blocked entries for $2 till $3"
fi

echo "found $entries number of entries" 
echo "Successfully got all Blocked entries"

exit 0

