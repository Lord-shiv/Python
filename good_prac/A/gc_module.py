import gc


def get_all_instances(of_class):
    instances = []
    for obj in gc.get_objects():
        if isinstance(obj, of_class):
            instances.append(obj)
    return instances
