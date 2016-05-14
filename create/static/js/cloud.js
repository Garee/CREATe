$(document).ready(function() {
    var words = [
        {word: "one", freq: 3425},
        {word: "two", freq: 500},
        {word: "three", freq: 475},
        {word: "four", freq: 3255},
        {word: "five", freq: 439},
        {word: "six", freq: 343},
        {word: "seven", freq: 325},
        {word: "eight", freq: 36353},
        {word: "nine", freq: 3525}
    ];
    
    var fill = d3.scale.category20();

    var layout = d3.layout.cloud()
        .size([800, 500])
        .words(words.map(function(d, i) {
            return {text: d.word, size: 50 + (i * 10)};
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