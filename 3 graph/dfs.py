# Рекурсивный алогритм поиска в глубину
def dfs(u, colors, weights):
    # u - индекс вершины
    # list цветов всех вершин, один для всего runtime программы
    # weights - list весов всех встречных рёбер
    # (изначально пуст)
    colors[u] = 'grey' # красим в серый цвет
    for v in adj_list[u]: # для всех вершин, смежных с текущей
        # запоминаем все встречные веса, и зануляем, чтобы не посчитать второй раз
        weights.append(weights_dict[frozenset([u, v])])
        weights_dict[frozenset([u, v])] = 'white'
        # если смежная вершина белая, то рекурсивно вызываем поиск из этой вершины
        if colors[v] == 'white':
            dfs(v, colors, weights)
    colors[u] = 'black' # в конце красим в чёрный
    return


if __name__ == "__main__":
    n, m = map(int, input().split())
    # множества смежных вершин для каждой вершины
    adj_list = [set() for _ in range(n)]
    # словарь весов
    # ключ - frozenset двух вершин,
    # обычное множество нельзя, потому что
    # изменяемый тип не может быть ключом
    # значение - int - вес ребра
    weights_dict = dict()
    # заполняем вспомогательные структуры
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_list[u].add(v)
        adj_list[v].add(u)
        weights_dict[frozenset([u, v])] = w
    # colors[i] хранит цвет i-й вершины
    colors = ['white'] * n
    # веса компонент связности
    cumm_weights = []
    for u in range(n):
        # запускаем поиск из каждой белой вершины
        # каждый запуск - новая компонента
        if colors[u] == 'white':
            weights = []
            dfs(u, colors, weights)
            cumm_weights.append(sum(weights))

    # в конце печатаем упорядоченные веса
    for w in sorted(cumm_weights):
        print(w)
