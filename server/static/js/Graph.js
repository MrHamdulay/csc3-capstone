function Graph() {
    this.E = 0;
    this.adj = {};
}

Graph.prototype.add_edge = function(v, w) {
    this._add_edge(v, w);
    this.E++;
}

Graph.prototype._add_edge = function(s, t) {
    if (typeof this.adj[s] == 'undefined')
        this.adj[s] = [];
    this.adj[s].push(t)
}

Graph.prototype.get_num_edges = function() {
    return this.E;
}

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

Graph.prototype.get_groups = function() {
    var c = 0;
    var islands = {};
    for (var key in this.adj) {
        var adj = this.adj[key];
        if (typeof islands[key] == 'undefined') {
            // get index from adj, otherwise set to c
            var has_c = false;
            for (var i = 0; i < adj.length; i++) {
                var w = adj[i];
                if (typeof islands[w.target] != 'undefined') {
                    islands[key] = islands[w.target];
                    has_c = true;
                    break;
                }
            }
            if (!has_c) {
                islands[key] = c;
                c++;
            }
        } else {
            // give all adjacent it's value
            for (var i = 0; i < adj.length; i++) {
                var w = adj[i];
                islands[w.target] = islands[key];
            }
        }
    }
    var result = new Array(c);
    var index;
    var c;
    for (var key in islands) {
        c = islands[key];
        if (typeof result[c] == 'undefined')
            result[c] = [];
        var adj = this.adj[key];
        for (var i = 0; i < adj.length; i++) {
            result[c].push({
                source: key,
                target: adj[i].target,
                confidence: adj[i].confidence,
                line_numbers: adj[i].line_numbers
            });
        }
    }
    return result
}
