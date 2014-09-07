class Node(object):
    """A node in the suffix tree.

    suffix_node
        the index of a node with a matching suffix, representing a suffix link.
        -1 indicates this node has no suffix link.

    strings_contained
        bitstring of strings the substring defined by the partial path
        of this edge is contained within

        e.g. if the path from root - current edge is 'aham'
        and 'aham' is in string 1 and string 2 the first bit and
        second bit will be set
    """
    def __init__(self):
        self.suffix_node = -1
        self.strings_contained = -1

    def __repr__(self):
        return "Node(suffix link: %d)"%self.suffix_node

class Edge(object):
    """An edge in the suffix tree.

    first_char_index
        index of start of string part represented by this edge

    last_char_index
        index of end of string part represented by this edge

    source_node_index
        index of source node of edge

    dest_node_index
        index of destination node of edge

    """
    def __init__(self, string, first_char_index, last_char_index, source_node_index, dest_node_index):
        self.string = string
        self.first_char_index = first_char_index
        self.last_char_index = last_char_index
        self.source_node_index = source_node_index
        self.dest_node_index = dest_node_index
        self.strings_contained = -1

    @property
    def length(self):
        return self.last_char_index - self.first_char_index

    def __repr__(self):
        return 'Edge(%d, %d, %d, %d, "%s")'% (self.source_node_index, self.dest_node_index
                                        ,self.first_char_index, self.last_char_index,
                                        self.string[self.first_char_index:min(self.last_char_index+1, 10)])


class Suffix(object):
    """Represents a suffix from first_char_index to last_char_index.

    source_node_index
        index of node where this suffix starts

    first_char_index
        index of start of suffix in string

    last_char_index
        index of end of suffix in string
    """
    def __init__(self, source_node_index, first_char_index, last_char_index):
        self.source_node_index = source_node_index
        self.first_char_index = first_char_index
        self.last_char_index = last_char_index

    @property
    def length(self):
        return self.last_char_index - self.first_char_index

    def explicit(self):
        """A suffix is explicit if it ends on a node. first_char_index
        is set greater than last_char_index to indicate this.
        """
        return self.first_char_index > self.last_char_index

    def implicit(self):
        return self.last_char_index >= self.first_char_index


class SuffixTree(object):
    """A suffix tree for string matching. Uses Ukkonen's algorithm
    for construction.
    """
    def __init__(self, string, case_insensitive=False):
        """
        string
            the string for which to construct a suffix tree
            or a list of strings if this is a generalised
            suffix tree
        """
        self.original_strings = [string]
        special = '$#'
        if isinstance(string, list):
            self.original_strings = string
            self.string_endpoints = []
            new_string = ''
            for i, s in enumerate(string):
                new_string += s+special[i]
                self.string_endpoints.append(new_string.find(special[i]))
            string = new_string

        self.string = string
        self.case_insensitive = case_insensitive
        self.N = len(string) - 1
        self.nodes = [Node()]
        self.edges = [{}]
        self.active = Suffix(0, 0, -1)
        if self.case_insensitive:
            self.string = self.string.lower()
        for i in range(len(string)):
            self._add_prefix(i)

        if len(self.original_strings) > 1:
            # precalculate LCS stuff
            self._precalculate_common_substrings()

    def __repr__(self):
        """
        Lists edges in the suffix tree
        """
        curr_index = self.N
        s = "\tStart \tEnd \tSuf \tFirst \tLast \tString\n"
        values = [e for edge in self.edges for e in edge.values()]
        values.sort(key=lambda x: x.source_node_index)
        for edge in values:
            if edge.source_node_index == -1:
                continue
            s += "\t%s \t%s \t%s \t%s \t%s \t"%(edge.source_node_index
                    ,edge.dest_node_index
                    ,self.nodes[edge.dest_node_index].suffix_node
                    ,edge.first_char_index
                    ,edge.last_char_index)


            top = min(curr_index, edge.last_char_index)
            s += self.string[edge.first_char_index:top+1] + "\n"
        return s

    def _add_prefix(self, last_char_index):
        """The core construction method.
        """
        last_parent_node = -1
        while True:
            parent_node = self.active.source_node_index
            if self.active.explicit():
                if self.string[last_char_index] in self.edges[self.active.source_node_index]:
                    # prefix is already in tree
                    break
            else:
                e = self.edges[self.active.source_node_index][self.string[self.active.first_char_index]]
                if self.string[e.first_char_index + self.active.length + 1] == self.string[last_char_index]:
                    # prefix is already in tree
                    break
                parent_node = self._split_edge(e, self.active)


            self.nodes.append(Node())
            self.edges.append({})
            e = Edge(self.string, last_char_index, self.N, parent_node, len(self.nodes) - 1)
            self._insert_edge(e)

            if last_parent_node > 0:
                self.nodes[last_parent_node].suffix_node = parent_node
            last_parent_node = parent_node

            if self.active.source_node_index == 0:
                self.active.first_char_index += 1
            else:
                self.active.source_node_index = self.nodes[self.active.source_node_index].suffix_node
            self._canonize_suffix(self.active)
        if last_parent_node > 0:
            self.nodes[last_parent_node].suffix_node = parent_node
        self.active.last_char_index += 1
        self._canonize_suffix(self.active)

    def _insert_edge(self, edge):
        self.edges[edge.source_node_index][self.string[edge.first_char_index]] = edge

    def _remove_edge(self, edge):
        self.edges[edge.source_node_index].pop(self.string[edge.first_char_index])

    def _split_edge(self, edge, suffix):
        self.nodes.append(Node())
        self.edges.append({})
        e = Edge(self.string, edge.first_char_index, edge.first_char_index + suffix.length, suffix.source_node_index, len(self.nodes) - 1)
        self._remove_edge(edge)
        self._insert_edge(e)
        self.nodes[e.dest_node_index].suffix_node = suffix.source_node_index  ### need to add node for each edge
        edge.first_char_index += suffix.length + 1
        edge.source_node_index = e.dest_node_index
        self._insert_edge(edge)
        return e.dest_node_index

    def _canonize_suffix(self, suffix):
        """This canonizes the suffix, walking along its suffix string until it
        is explicit or there are no more matched nodes.
        """
        if not suffix.explicit():
            e = self.edges[suffix.source_node_index][self.string[suffix.first_char_index]]
            if e.length <= suffix.length:
                suffix.first_char_index += e.length + 1
                suffix.source_node_index = e.dest_node_index
                self._canonize_suffix(suffix)

    def _precalculate_common_substrings(self, curr_node=0):
        """ returns bit string of contained strings """
        if self.nodes[curr_node].strings_contained != -1:
            return self.nodes[curr_node].strings_contained

        common = 0
        for edge in self.edges[curr_node].itervalues():
            if not edge:
                continue
            new_common = 0
            new_common |= self._precalculate_common_substrings(edge.dest_node_index)
            edge.strings_contained = new_common
            # only choose the lowest i
            for i, point in enumerate(self.string_endpoints):
                if edge.first_char_index <= point <= edge.last_char_index:
                    new_common |= 1 << i
                    break
            common |= new_common

        self.nodes[curr_node].strings_contained = common
        return common



    # Public methods
    def edge_string(self, edge):
        return self.string[edge.first_char_index:edge.last_char_index+1]

    def find_substring(self, substring):
        """Returns the index of substring in string or -1 if it
        is not found.
        """
        if not substring:
            return -1
        if self.case_insensitive:
            substring = substring.lower()
        curr_node = 0
        i = 0
        while i < len(substring):
            edge = self.edges[curr_node].get(substring[i])
            if not edge:
                return -1
            ln = min(edge.length + 1, len(substring) - i)
            if substring[i:i + ln] != self.string[edge.first_char_index:edge.first_char_index + ln]:
                return -1
            i += edge.length + 1
            curr_node = edge.dest_node_index
        return edge.first_char_index - len(substring) + ln

    def has_substring(self, substring):
        return self.find_substring(substring) != -1

    def longest_common_substring(self, current_node=0):
        strings_contained = 0
        for i in xrange(len(self.original_strings)):
            strings_contained |= 1<<i

        longest = ''
        for edge in self.edges[current_node].itervalues():
            if not edge:
                continue
            if edge.strings_contained == strings_contained:
                potential_longest = self.string[edge.first_char_index:edge.last_char_index+1]
                edge_string = self.longest_common_substring(edge.dest_node_index)
                if len(potential_longest) + len(edge_string) > len(longest):
                    longest = potential_longest+edge_string


        return longest

    def substrings_longer_than(self, min_length, current_node=0):

        for edge in self.edges[current_node].itervalues():
            if not edge or edge.strings_contained != strings_contained:
                continue
            edge_begin = self.string[edge.first_char_index:edge.last_char_index+1]

            for edge_potential in self.substrings_longer_than(min_length - edge.length-1, edge.dest_node_index):
                if len(edge_potential) + edge.length+1 >= min_length:
                    yield end_begin + edge_potential
