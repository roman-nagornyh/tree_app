import typing


class TreeStore:
    def __init__(self, items):
        self.__items = items[:]
        self.__dict_items = {v['id']: v for v in items}

    def getAll(self):
        return self.__items

    def getItem(self, id) -> dict | bool:
        res: list | bool = self.__dict_items.get(id, False)
        return res if res else False

    def getChildren(self, id):
        return [x for x in self.__items if x['parent'] == id]

    def getParentAll(self, id, items=None):
        if items is None:
            items = []
        el = self.getItem(id)
        if not el:
            return False
        items.append(el)
        if el['parent'] == 'root':
            return items
        return self.getParentAll(el['parent'], items)
