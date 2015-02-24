def pretty_list_from_queryset(items):
    if len(items) < 2:
        return str(items.first())
    else:
        return ", ".join([str(i) for i in items if i != items.last()]) + \
               " and " + str(items.last())
