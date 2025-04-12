def helper(work):
    work_in_memory = work
    def helper(work):
        return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
    return helper

helper_ = helper("homework")
print(helper_)
print(helper_("cleaning"))
print(helper_("driving"))