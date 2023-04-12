from classes import TreeStore

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

ts = TreeStore(items)
print(f'Получение всех элементов дерева:{ts.getAll()}')
print('')
print(f'Получение элемента 7:{ts.getItem(7)}')
print(f'Получение получение потомков элемента 4: {ts.getChildren(4)}')
print('')
print(f'Получение получение потомков элемента 5 :{ts.getChildren(5)}')
print('')
print(f'Получение дерева для элемента 7 :{ts.getParentAll(7)}')



