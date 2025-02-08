
class TrafficScore:

    def __init__(self):
        self.thread_level = 0
        self.human_factor = 0
        self.bot_factor = 0
        self.applied_rules = []
        self.redirected = False

    def __str__(self):
        return "Human: {0}%, Bot: {1}%, THREAD: {2}, applied {3} rules".format(self.human_factor,
                                                                               self.bot_factor,
                                                                               self.thread_level,
                                                                               len(self.applied_rules))

    def apply_rule(self, rule, actions):
        for action in actions:
            new_value = getattr(self, action['target']) + action['value']
            setattr(self, action['target'], new_value)

        self.applied_rules.append(rule_info(rule, actions))

    def set_flag(self, rule, value, target):
        setattr(self, target, value)
        self.applied_rules.append(rule_info(rule, {"value": value, "target": target}))

class rule_info:
    def __init__(self, rule_string, actions):
        self.rule_string = rule_string
        self.actions = actions

    def __str__(self):
        string = '::{0} -- '.format(self.rule_string)
        for action in self.actions:
            string += '{0} : +{1}, '.format(action['target'], action['value'])
        return string
