var inc = (tNow-tFirst)/(window.innerWidth*.8)
var time = tNow
var activeTracker = act.slice()
var graphs = []
var names = ["2-3","2-4","3-5","4-6","5-7","6-8","7-9"]
var pad = 5
var rectHeight = Math.max((window.innerHeight-65)*.06,window.innerHeight*.045)
var fontSize = Math.min(rectHeight*5/3,window.innerWidth/15)
var buff = Math.min(5,rectHeight/3)
var dateSize = Math.min(window.innerWidth*.04,window.innerHeight*.075,15)


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
    .attr("width", window.innerWidth-pad)
    .attr("height", Math.abs(window.innerHeight-pad));

var date0 = svgContainer.append("text")
    .text(new Date(tFirst*1000).toDateString())
    .attr("x",pad + fontSize*1.5)
    .attr("y",pad + dateSize*1.15)
    .style("font-size",dateSize+"px")
    .style("text-anchor","start");
var date1 = svgContainer.append("text")
    .text(new Date(tNow*1000).toDateString())
    .attr("x",pad + fontSize*1.5 + window.innerWidth*.8)
    .attr("y",pad + dateSize*1.15)
    .style("font-size",dateSize+"px")
    .style("text-anchor","end");

for (var n = 0; n < graphs.length; n++) {
    var l = graphs[n].length
    var positioner = 0
   
    var upTime = 0
    var downTime = 0
    for (var g = l-1; g >= 0; g--) {
	var rect = svgContainer.append("rect")
	    .attr("x",fontSize*1.5 + pad + positioner)
	    .attr("y",dateSize*1.2 + buff*n + pad + rectHeight*n)
	    .attr("width", graphs[n][g])
	    .attr("height", rectHeight);
	if (activeTracker[n] == l%2) {
	    rect.attr("fill", "green")
	    upTime += graphs[n][g]
	}
	else {
	    rect.attr("fill", "red")
	    downTime += graphs[n][g]
	}
	activeTracker[n] = !activeTracker[n]
	positioner += graphs[n][g]
    }
    var pctUp = Math.round(upTime*100/(upTime + downTime))+'%'

    var upTime = svgContainer.append("text")
	.text(pctUp)
	.attr("x",fontSize*1.5 + pad)
	.attr("y",dateSize*1.2 + buff*n + pad + rectHeight*(n+.5))
	.attr("dx",".35em")
	.attr("dy",".35em")
	.style("font-size",rectHeight+"px")
	.style("text-anchor","start")
	.style("fill","white");
    
    var arrow = svgContainer.append("text")
	.attr("x",fontSize*1.5 + pad + window.innerWidth*.8)
	.attr("y",dateSize*1.2 + buff*n + pad + rectHeight*(n+.5))
	.attr("dx",".35em")
	.attr("dy",".35em")
	.style("font-size",fontSize+"px")
	.style("font-weight", "bold")
	.style("text-anchor","middle");
    if (n%2 == 0) {
	arrow.text("↗");
	var text = svgContainer.append("text")
	    .attr("x",pad)
	    .attr("y",dateSize*1.2 + buff*(n+1) + pad +rectHeight*(n+1))
	    .attr("dy",".35em")
	    .style("font-size",fontSize+"px")
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
    
}

window.onresize = function(){ location.reload(); }