import config


def filter_attack_multiple_domains(data_object, al=False):
    def ip_multi_domains(entries):
        found_domains = []
        for e in entries:
            m = e.clientRequestHTTPHost in config.domains and (config.domains[e.clientRequestHTTPHost] or al)
            if (e.clientRequestHTTPHost not in found_domains) and m:
                found_domains.append(e.clientRequestHTTPHost)

                if len(found_domains) >= 2:
                    return True

        return False

    return {k: v for (k, v) in data_object.ip_dict.items() if ip_multi_domains(v)}


