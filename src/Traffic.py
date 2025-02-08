from datetime import datetime as DateTime
from .TrafficScore import TrafficScore


class Traffic:

    traffic_score = TrafficScore()

    def __init__(self,
                 datetime,
                 cacheStatus,
                 clientASNDescription,
                 clientAsn,
                 clientCountryName,
                 clientDeviceType,
                 clientIP,
                 clientRequestHTTPHost,
                 clientRequestHTTPMethodName,
                 clientRequestHTTPProtocol,
                 clientRequestPath,
                 clientRequestQuery,
                 clientRequestScheme,
                 clientSSLProtocol,
                 edgeResponseStatus,
                 leakedCredentialCheckResult,
                 originResponseDurationMs,
                 requestSource,
                 securityAction,
                 securitySource,
                 userAgent,
                 clientRequestReferer,
                 clientRefererHost,
                 xRequestedWith,
                 originIP,
                 originASN,
                 originResponseStatus,
                 ):
        self.cacheStatus = cacheStatus
        self.clientASNDescription = clientASNDescription
        self.clientAsn = clientAsn
        self.clientCountryName = clientCountryName
        self.clientDeviceType = clientDeviceType
        self.clientIP = clientIP
        self.clientRequestHTTPHost = clientRequestHTTPHost
        self.clientRequestHTTPMethodName = clientRequestHTTPMethodName
        self.clientRequestHTTPProtocol = clientRequestHTTPProtocol
        self.clientRequestPath = clientRequestPath
        self.clientRequestQuery = clientRequestQuery
        self.clientRequestScheme = clientRequestScheme
        self.clientSSLProtocol = clientSSLProtocol
        self.clientRequestReferer = clientRequestReferer
        self.clientRefererHost = clientRefererHost
        self.datetime = DateTime.strptime(datetime, '%Y-%m-%dT%H:%M:%SZ')
        self.edgeResponseStatus = edgeResponseStatus
        self.leakedCredentialCheckResult = leakedCredentialCheckResult
        self.originResponseDurationMs = originResponseDurationMs
        self.originIP = originIP
        self.originASN = originASN
        self.originResponseStatus = originResponseStatus
        self.requestSource = requestSource
        self.securityAction = securityAction
        self.securitySource = securitySource
        self.userAgent = userAgent
        self.xRequestedWith = xRequestedWith

    def __str__(self):
        block = " " if self.securityAction == "unknown" else "B"
        return "{0} - {1} at {2} AS: {5} using {4} ---- {3}".format(self.clientIP,
                                                                    self.clientRequestHTTPHost,
                                                                    self.datetime,
                                                                    block,
                                                                    self.clientRequestHTTPMethodName,
                                                                    self.clientRequestHTTPProtocol)

    # Replace with vars(Traffic).items()
    def full_string(self):
        data = dict()
        data["CacheStatus"] = self.cacheStatus
        data["ClientASNDescription"] = self.clientASNDescription
        data["clientASN"] = self.clientAsn
        data["clientCountryName"] = self.clientCountryName
        data["clientDeviceType"] = self.clientDeviceType
        data["clientIP"] = self.clientIP
        data["clientRequestHTTPHost"] = self.clientRequestHTTPHost
        data["clientRequestHTTPMethodName"] = self.clientRequestHTTPMethodName
        data["clientRequestHTTPProtocol"] = self.clientRequestHTTPProtocol
        data["clientRequestPath"] = self.clientRequestPath
        data["clientRequestQuery"] = self.clientRequestQuery
        data["datetime"] = self.datetime
        data["EdgeResponseStatus"] = self.edgeResponseStatus
        data["LeakedCredentialCheckResult"] = self.leakedCredentialCheckResult
        data["originResponseDurationMs"] = self.originResponseDurationMs
        data["requestSource"] = self.requestSource
        data["securityAction"] = self.securityAction
        data["securitySource"] = self.securitySource
        data["userAgent"] = self.userAgent
        data["clientRequestScheme"] = self.clientRequestScheme
        data["clientSSLProtocol"] = self.clientSSLProtocol

        return data
