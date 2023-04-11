class TreeStore:
    def __init__(self, items: list[dict]):
        self.__items = items

    def getAll(self):
        return self.__items

    def getItem(self, id):
        return filter(lambda x: x['id'] == id, self.__items)

    def getChildren(self, id):
        pass


class TreeStore2:
    def __init__(self, items: list[dict]):
        self.__items = items
        self.__dict_items = {v['id']: v | {'children': (x for x in items if x['parent'] == v['id'])} for v in items}

    def getAll(self):
        return self.__items

    def getItem(self, id, is_delete=False):
        res = self.__dict_items.get(id, False)
        return {**res}


    def getChildren(self, id):
        list(self.__dict_items.get(id, []).get('children'))

