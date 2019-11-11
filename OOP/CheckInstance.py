def check_instance(obj, cls):
    return check_subclass(type(obj), cls)
    # return cls in type(obj).mro()

def check_subclass(child, base):
    # return base in child.mro()
    for direct_base in child.__bases__:
        if base == direct_base:
            return True
        return check_subclass(direct_base, base)
    return False