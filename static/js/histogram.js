var inc = (tNow-tFirst)/(window.innerWidth*.8)
var time = tNow
var activeTracker = act.slice()
var graphs = []
var names = ["2-3","2-4","3-5","4-6","5-7","6-8","7-9"]
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
    .attr("width", window.innerWidth-10)
    .attr("height", Math.abs(window.innerHeight-10));

for (var n = 0; n < graphs.length; n++) {
    var l = graphs[n].length
    var positioner = 0
    var arrow = svgContainer.append("text")
	.attr("x",(window.innerHeight-65)*.18 + 10 + window.innerWidth*.8)
	.attr("y",5*(n+1)+10+(window.innerHeight-65)*.06*(n+1))
	.attr("dy","0em")
	.style("font-size",(window.innerHeight-65)*.1+"px")
	.style("font-weight", "bold")
	.style("text-anchor","start");
    if (n%2 == 0) {
	arrow.text("↗");
	var text = svgContainer.append("text")
	    .attr("x",10)
	    .attr("y",5*(n+1)+10+(window.innerHeight-65)*.06*(n+1))
	    .attr("dy",".35em")
	    .style("font-size",(window.innerHeight-65)*.1+"px")
	    .style("text-anchor","start")
	    .text(names[n/2]);
    }
    else
	arrow.text("↘");
    
    if (act[n]) {
	arrow.style("fill","green")
    }
    else {
	arrow.style("fill","red")
    }
	    
    for (var g = l-1; g >= 0; g--) {
	var rect = svgContainer.append("rect")
	    .attr("x",(window.innerHeight-65)*.18 + 10 + positioner)
	    .attr("y",5*n+10+(window.innerHeight-65)*.06*n)
	    .attr("width", graphs[n][g])
	    .attr("height", (window.innerHeight-65)*.06);
	if (activeTracker[n] == l%2)
	    rect.attr("fill", "green")
	else
	    rect.attr("fill", "red")
	activeTracker[n] = !activeTracker[n]
	positioner += graphs[n][g]
    }
}

window.onresize = function(){ location.reload(); }