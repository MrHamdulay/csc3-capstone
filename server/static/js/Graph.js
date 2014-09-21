/**
 * Graph.js
 * Author: Jarred de Beer
 * Date: 22 September 2014
 *
 * Description:
 * A simple Graph data structure to take the Pairs of students and generate a graph
 * with nodes as the student numbers and edges as the Pair connection.
 * This contains a method to generate groups of students from the graph topoplogy
 * by traversing the graph and identifying isolated clusters of nodes.
 **/

// constructor
function Graph() {
    this.E = 0;
    this.adj = {};
}

// private and public methods.
//
// private methods are prefixed with an underscore.
// Extends the Graph prototype object mimicking the declaration of methods for the Graph 'class'

// Add an edge from node v to node w
Graph.prototype.add_edge = function(v, w) {
    this._add_edge(v, w);
    this.E++;
}

Graph.prototype._add_edge = function(s, t) {
    if (typeof this.adj[s] == 'undefined')
        this.adj[s] = [];
    this.adj[s].push(t)
}

// Get the number of edges in the graph
Graph.prototype.get_num_edges = function() {
    return this.E;
}

// Get the source and target pair objects from the edges to be used with d3
// when rendering the tables list
Graph.prototype.get_d3_json = function() {
    var json = [];
    var adj;
    for (var key in this.adj) {
        adj = this.adj[key]
        for (var i = 0; i < adj.length; i++) {
            json.push({source: key, target: adj[i]});
        }
    }
    return json;
}

// Get the groups from the Graph topology.
// Traverses the graph and finds isolated clusters of nodes which are the groups
Graph.prototype.get_groups = function() {
    var c = 0; // count of clusters
    var clusters = {};
    for (var key in this.adj) {
        var adj = this.adj[key];
        if (typeof clusters[key] == 'undefined') {
            // get index from adj, otherwise set to c
            var has_c = false;
            for (var i = 0; i < adj.length; i++) {
                var w = adj[i];
                if (typeof clusters[w.target] != 'undefined') {
                    clusters[key] = clusters[w.target];
                    has_c = true;
                    break;
                }
            }
            if (!has_c) {
                clusters[key] = c;
                c++;
            }
        } else {
            // give all adjacent it's value
            for (var i = 0; i < adj.length; i++) {
                var w = adj[i];
                clusters[w.target] = clusters[key];
            }
        }
    }

    var result = new Array(c);
    var index;
    var c;
    for (var key in clusters) {
        c = clusters[key];
        if (typeof result[c] == 'undefined')
            result[c] = [];
        var adj = this.adj[key];
        for (var i = 0; i < adj.length; i++) {
            result[c].push({
                source: key,
                target: adj[i].target,
                confidence: adj[i].confidence,
                line_numbers: adj[i].line_numbers,
                source_id: adj[i].source_id,
                target_id: adj[i].target_id
            });
        }
    }
    return result
}
