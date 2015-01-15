console.log('fuck yall');

var inc = (tNow-tFirst)/(window.innerWidth*.8)
var time = tNow
var activeTracker = act.slice()
var graphs = []
for (var n = 0; n < hist.length; n++) {
    graphs[graphs.length] = [0]
}

while (time >= tFirst) {
    for (var n = 0; n < hist.length; n++) {
	if (trackers[n] >= 0 && time < hist[n][trackers[n]]) {
	    graphs[n][graphs[n].length] = 0
	    trackers[n] --
	}
	graphs[n][graphs[n].length-1] += 1
    }
	time -= inc;
}
var svgContainer = d3.select("body").append("svg")
    .attr("width", window.innerWidth)
    .attr("height", Math.abs(window.innerHeight - 100));

for (var n = 0; n < graphs.length; n++) {
    var l = graphs[n].length
    var positioner = 0
    for (var g = l-1; g >= 0; g--) {
	var rect = svgContainer.append("rect")
	    .attr("x",10+positioner)
	    .attr("y",5*n+10+window.innerHeight*.05*n)
	    .attr("width", graphs[n][g])
	    .attr("height", window.innerHeight*.05);
	if (activeTracker[n] == l%2)
	    rect.attr("fill", "green")
	else
	    rect.attr("fill", "red")
	activeTracker[n] = !activeTracker[n]
	positioner += graphs[n][g]
    }
}

window.onresize = function(){ location.reload(); }