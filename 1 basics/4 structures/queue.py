def new_queue():
    return {'size': 0,
            'head': None}

def new_node(value):
    return {'value': value,
            'next': None}

def insert_head(queue, value):
    tmp = new_node(value)
    if queue['head'] is None:
        queue['head'] = tmp
        queue['size'] += 1
        return
    tmp['next'] = queue['head']
    queue['head'] = tmp
    queue['size'] += 1

def print_queue(queue):
    cur = queue['head']
    while cur is not None:
        print(cur['value'], end=' ')
        cur = cur['next']


if __name__ == "__main__":
    q = new_queue()
    for i in range(100, 0, -1):
        insert_head(q, i)
    print_queue(q)

