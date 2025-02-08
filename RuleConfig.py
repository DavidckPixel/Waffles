AlphabeticalRuleConfig = {
    "AlphRule1": {
        "description": "Request Path/Query-String are applied to subdomains Alphabetically",
        "actions": [{
            "value": 0.9,
            "target": "bot_factor"
        }]
    }
}

AttackMultiDomainConfig = {
    "MultiDom1": {
        "description": "IP attacks multiple domains markt as private",
        "actions": [{
            "value": 0.3,
            "target": "thread_level"
        }]
    }
}

CommonPathRuleConfig = {
    "CommPath1": {
        "description": "IP visits path that are commonly visited by bots",
        "actions": [{
            "value": 0.4,
            "target": "bot_factor"
        }, {
            "value":-0.2,
            "target": 'thread_level'
        }]
    },
    "CommPath2": {
        "description": "IP visits uncommon path",
        "actions": [{
            "value": 0.2,
            "target": "thread_level"
        }]
    }
}

HTTPVersionRuleConfig = {
    "HTTPVer1": {
        "description": "The IP uses three different versions of HTTP",
        "actions": [{
            "value": 0.3,
            "target": "bot_factor"
        }, {
            "value": 0.2,
            "target": "thread_level"
        }]
    },
    "HTTPVer2": {
        "description": "The IP uses two different versions of HTTP",
        "actions": [{
            "value": 0.3,
            "target": "bot_factor"
        }, {
            "value": 0.2,
            "target": "thread_level"
        }]
    },
    "HTTPVer3": {
        "description": "The IP only uses HTTP version 1.1",
        "actions": [{
            "value": 0.3,
            "target": "bot_factor"
        }]
    },
    "HTTPVer4": {
        "description": "The IP uses HTTP 3",
        "actions": [{
            "value": 0.2,
            "target": "human_factor"
        }, {
            "value": 0.3,
            "target": "thread_level"
        }]
    }
}

NightRuleConfig = {
    "Night1": {
        "description": "The IP only sents packages during local night",
        "actions": [{
            "value": 0.5,
            "target": "bot_factor"
        }]
    },
    "Night2": {
        "description": "The IP only sents packages during local day",
        "actions": [{
            "value": 0.2,
            "target": "human_factor"
        }]
    },
    "Night3": {
        "description": "The IP sents packages during both local day & night",
        "actions": [{
            "value": 0.2,
            "target": "bot_factor"
        }]
    }
}

RedirectedRuleConfig = {
    "Redir1": {
        "description": "All Requests were properly redirected",
        "actions": [{
            "value": 0.3,
            "target": "human_factor"
        }]
    },
    "Redir2": {
        "description": "No Requests were properly redirected",
        "actions": [{
            "value": 0.7,
            "target": "bot_factor"
        }]
    },
    "Redir3": {
        "description": "Some Requests followed re-directs, not all",
        "actions": [{
            "value": 0.2,
            "target": "human_factor"
        }, {
            "value": 0.2,
            "target": "thread_level"
        }]
    }
}

TimeRuleConfig = {
    "Time1": {
        "description": "IP visits were too quick in succession",
        "actions": [{
            "value": 1,
            "target": "bot_factor"
        }]
    }
}

TLSVariationRuleConfig = {
    "TLS1": {
        "description": "IP uses 3 different TLS versions",
        "actions": [{
            "value": 0.2,
            "target": "thread_level"
        }, {
            "value": 0.3,
            "target": "bot_factor"
        }]
    },
    "TLS2": {
        "description": "IP uses no TLS and a TLS versions, caused by automatic upgrade",
        "actions": [{
            "value": 0.5,
            "target": "bot_factor"
        }]
    },
    "TLS3": {
        "description": "IP uses no TLS and a TLS versions, Sporedic switcing",
        "actions": [{
            "value": 0.1,
            "target": "thread_level"
        }]
    },
    "TLS4": {
        "description": "IP uses two TLS versions",
        "actions": [{
            "value": 0.3,
            "target": "bot_factor"
        }, {
            "value": 0.2,
            "target": "thread_level"
        }]
    },
    "TLS5": {
        "description": "IP uses either only TLSv1.2 or TLSv1.3",
        "actions": [{
            "value": 0.1,
            "target": "human_factor"
        }, {
            "value": 0.1,
            "target": "thread_level"
        }]
    },
    "TLS6": {
        "description": "IP never uses TLS",
        "actions": [{
            "value": 0.5,
            "target": "bot_factor"
        }]
    },
    "TLS7": {
        "description": "IP visits were too quick in succession",
        "actions": [{
            "value": 1,
            "target": "bot_factor"
        }]
    },
    "TLS8": {
        "description": "IP visits were too quick in succession",
        "actions": [{
            "value": 1,
            "target": "bot_factor"
        }]
    }
}

UnknownDomainRuleConfig = {
    "Unkn1": {
        "description": "IP visits domain that is not in known domains",
        "actions": [{
            "value": 0.5,
            "target": "thread_level"
        }]
    }
}

UserAgentSwitchRuleConfig = {
    "UsSwitch1": {
        "description": "IP constantly switches from user agent",
        "actions": [{
            "value": 1,
            "target": "bot_factor"
        }]
    },
    "UsSwitch2": {
        "description": "IP uses constant user agent",
        "actions": [{
            "value": 0.1,
            "target": "human_factor"
        }]
    }
}

AttacksApexRuleConfig = {
    "AtApex1": {
        "description": "IP only targets second apex",
        "actions": [{
            "value": 0.3,
            "target": "thread_level"
        }]
    },
    "AtApex2": {
        "description": "IP only targets apex",
        "actions": [{
            "value": 0.5,
            "target": "bot_factor"
        }]
    },
    "AtApex3": {
        "description": "IP targets apex more then second apex",
        "actions": [{
            "value": 0.2,
            "target": "bot_factor"
        }]
    },
    "AtApex4": {
        "description": "IP targets second apex more then target apex",
        "actions": [{
            "value": 0.1,
            "target": "thread_level"
        }]
    }
}

AverageTimeRuleConfig = {
    "AvTime1": {
        "description": "IP average time between messages is less then 1 second",
        "actions": [{
            "value": 0.5,
            "target": "bot_factor"
        }]
    },
    "AvTime2": {
        "description": "IP average time between messages is less then 10 seconds",
        "actions": [{
            "value": 0.0,
            "target": "bot_factor"
        }]
    },
    "AvTime3": {
        "description": "IP average time between messages is more then 1000 seconds",
        "actions": [{
            "value": 0.0,
            "target": "bot_factor"
        }]
    },
    "AvTime4": {
        "description": "IP average time between message is more then 10000 seconds",
        "actions": [{
            "value": 0.0,
            "target": "bot_factor"
        }]
    }
}

MultiDayRuleConfig = {
    "MuDay1": {
        "description": "IP takes breaks longer then 12 hours between messages",
        "actions": [{
            "value": 0.1,
            "target": "thread_level"
        }]
    }
}

PercentageBlockedRuleConfig = {
    "PerBl1": {
        "description": "IP has comparable amount of blocked VS allowed requests",
        "actions": [{
            "value": 0.5,
            "target": "bot_factor"
        }]
    },
    "PerBl2": {
        "description": "IP contains mostly blocked traffic",
        "actions": [{
            "value": 0.7,
            "target": "bot_factor"
        }]
    },
    "PerBl3": {
        "description": "IP contains mostly non-blocked traffic",
        "actions": [{
            "value": 0.1,
            "target": "thread_level"
        }]
    },
    "PerBl4": {
        "description": "IP only sent 1 blocked message",
        "actions": [{
            "value": 1,
            "target": "bot_factor"
        }, {
            "value": -1,
            "target": "thread_level"
        }]
    }
}

MultiIPAsnConfig = {
    "MuAsn": {
        "description": "IP belongs to an AS which attacked with multiple IP's",
        "actions": [{
            "value": 0.1,
            "target": "thread_level"
        }]
    }
}

OperCountryRuleConfig = {
    "OpCo": {
        "description": "IP originates from known Country",
        "actions": [{
            "value": 0.3,
            "target": "thread_level"
        }]
    }
}

ExpectedBrowserRule = {
    "ExpBr1": {
        "description": "IP only uses commonly used browsers",
        "actions": [{
            "value": 0.1,
            "target": "thread_level"
        }, {
            "value": 0.1,
            "target": "human_factor"
        }]
    },
    "ExpBr2": {
        "description": "IP does not use any known browsers",
        "actions": [{
            "value": 0.8,
            "target": "bot_factor"
        }]
    }
}
