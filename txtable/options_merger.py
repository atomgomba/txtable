class OptionsMerger(type):
    options = {}

    def __new__(mcs, name, bases, classdict):
        new = type.__new__(mcs, name, bases, dict(classdict))
        if not hasattr(new, "options"):
            new.options = {}
        if bases:
            for base in bases:
                if hasattr(base, "options"):
                    options = base.options.copy()
                    options.update(new.options)
                    new.options = options
        return new
