$(document).ready(function() {
    $("#vis-container").transition("fly up");
    
    var words = [
        "copyright",
        "piracy",
        "music",
        "digital",
        "software",
        "study",
        "use",
        "sharing",
        "rights",
        "file",
        "law",
        "paper",
        "between",
        "intellectual",
        "property",
        "model",
        "economic",
        "consumers",
        "industry",
        "results",
        "legal",
        "analysis",
        "research",
        "but",
        "works",
        "social",
        "online",
        "sales",
        "behavior",
        "internet",
        "whether",
        "protection",
        "been",
        "policy",
        "article",
        "downloading",
        "market",
        "other",
        "about",
        "impact"
    ];
    
    var fill = d3.scale.category20();

    var layout = d3.layout.cloud()
        .size([800, 500])
        .words(words.map(function(d, i) {
            return {text: d, size: (70 - i)};
        }))
        .padding(5)
        .rotate(function() { return ~~(Math.random() * 2) * 90; })
        .font("Impact")
        .fontSize(function(d) { return d.size; })
        .on("end", draw);

    layout.start();

    function draw(words) {
        d3.select("#vis").append("svg")
            .attr("width", layout.size()[0])
            .attr("height", layout.size()[1])
            .append("g")
            .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
            .selectAll("text")
            .data(words)
            .enter().append("text")
            .style("font-size", function(d) { return d.size + "px"; })
            .style("font-family", "Impact")
            .style("fill", function(d, i) { return fill(i); })
            .attr("text-anchor", "middle")
            .attr("transform", function(d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
            })
            .text(function(d) { return d.text; });
    }
});