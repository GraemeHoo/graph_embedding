
def _get_order_degreelist_node(self, root, max_num_layers=None):
    if max_num_layers is None:
        max_num_layers = float('inf')

    ordered_degree_sequence_dict = {}
    visited = [False] * len(self.graph.nodes())
    queue = deque()
    level = 0
    queue.append(root)
    visited[root] = True

    while (len(queue) > 0 and level <= max_num_layers):

        count = len(queue)
        if self.opt1_reduce_len:
            degree_list = {}
        else:
            degree_list = []
        while (count > 0):

            top = queue.popleft()
            node = self.idx2node[top]
            degree = len(self.graph[node])

            if self.opt1_reduce_len:
                degree_list[degree] = degree_list.get(degree, 0) + 1
            else:
                degree_list.append(degree)

            for nei in self.graph[node]:
                nei_idx = self.node2idx[nei]
                if not visited[nei_idx]:
                    visited[nei_idx] = True
                    queue.append(nei_idx)
            count -= 1
        if self.opt1_reduce_len:
            orderd_degree_list = [(degree, freq)
                                  for degree, freq in degree_list.items()]
            orderd_degree_list.sort(key=lambda x: x[0])
        else:
            orderd_degree_list = sorted(degree_list)
        ordered_degree_sequence_dict[level] = orderd_degree_list
        level += 1

    return ordered_degree_sequence_dict