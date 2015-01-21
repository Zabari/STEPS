console.log("hi");

var escList = ["up23","down23","up24","down24","up35","down35","up46","down46","up57","down57","up68","down68","up79","down79"];

window.onload = function() {
    for (var i = 0; i < escList.length; i++) {
	document.getElementById(escList[i]).getSVGDocument(document).getElementsByTagName("path")[0].attributes[0].value = states[i]
    }
};
