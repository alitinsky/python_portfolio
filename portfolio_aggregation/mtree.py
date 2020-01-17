
class MNode:
    #  Class for Node
    """
     node_id  : string    node_id
     name : string      node name
     children_id  : list    list of childen id
     parent_id  : str
    """
    def __init__(self, node_id:str, name: str = None, children_id: list = None):
        self._node_id = node_id
        self._name = name
        self._children_id = children_id
        self._parent_id = None

    def get_node_id(self):
        return self._node_id

    def set_parent_id(self, parent_id: str):
        self._parent_id = parent_id

    def get_parent_id(self):
        return self._parent_id

    def set_children_id(self, children_id: list):
        self._children_id = children_id

    def get_children_id(self):
        return self._children_id

    def set_name(self, name: str):
        self._name = name

    def get_name(self):
        return self._name

    def add_props(self, name, children_id):
        self._name = name
        self._children_id = children_id

    def set_props(self, name, children_id):
        self._name = name
        self._children_id = children_id

    def __repr__(self):
        return '{} {} {} ==>>  {} '.format(self._node_id, self._name,
                                                self._parent_id,  self._children_id)

    def __str__(self):
        return '{} {} {} ==>>  {}'.format(self._node_id, self._name,
                                                 self._parent_id, self._children_id)


class MTree:
    ''' Class for MultiNode Tree.
       Attributes
       ==========
       _nodes :  dict  dictionary of all nodes
    '''
    def __init__(self):
        self._nodes = {}

    def add_node(self, node):
        ''' add Node to a tree
        '''
        node_id = node['id']
        name = node['name']
        children_id = node.get('children')
        if node_id in self._nodes:
            self._nodes[node_id].set_props(name=name, children_id=children_id)
        else:
            self._nodes[node_id] = MNode(node_id, name, children_id)

        if children_id is None:
            return

        for child_id in children_id:
            m_node = self._nodes[child_id] if child_id in  self._nodes.keys() else MNode(child_id)
            m_node.set_parent_id(node_id)
            self._nodes[child_id] = m_node

    def get_node_path(self, node_id: str):
        """ get a path from terminal node to top parent
        :param node_id:  str node id
        :return:  list of node id on the path from node to top parent
        """
        path = [node_id]
        while True:
            if node_id:
                node = self._nodes[node_id]
                parent_id = node.get_parent_id()
                if parent_id:
                    path.append(parent_id)
                    node_id = parent_id
                else:
                    break

        path.reverse()
        return path

    def get_term_nodes(self):
        """  get a list of terminal nodes id
        :return:  list of terminal nodes id
        """
        term_ids = []
        for node in self._nodes.values():
            if node.get_children_id() is None:
                term_ids.append(node.get_node_id())
        return term_ids

    def node2row(self, aggr_key, node_path):
        """
        :param aggr_key:  aggregation Base Key for example '"'SECTOR'
        :param node_id:  node_id
        :param node_path: list that represents path from node to top parent
        :return:  row_dict
        """
        row_dict = {}
        for (i, item) in enumerate(node_path):
            col_name = '{}-{}'.format(aggr_key, i)
            sect_name = self._nodes[item].get_name()
            row_dict[col_name] = sect_name
        return row_dict

    def print_nodes(self):
        for nd in self._nodes.values():
            print(nd)

    def get_node(self, node_id):
        ''' get a node based on node id
        '''
        return self._nodes[node_id]

    def get_nodes(self):
        return self._nodes


