var escalators;
var upOn = "static/img/UpOn.png"
var upOff = "static/img/UpOff.png"
var downOn = "static/img/DownOn.png"
var downOff = "static/img/DownOff.png"

var getRandomBoolean = function(p) {
    return (Math.random() > p);
};

var loadData = function() {//simulate loading escalator data
    escalators = new Array(7);
    for (var x = 0; x < 7; x++) {
	escalators[x] = new Array(2);
	for (var y = 0; y < 2; y++) {
	    escalators[x][y] = getRandomBoolean(.5);
	}
    }
};

var reloadData = function() {//simulate loading escalator data
    for (var x = 0; x < 7; x++) {
	for (var y = 0; y < 2; y++) {
	    if (getRandomBoolean(.9)) {
		escalators[x][y] = !escalators[x][y];
	    }
	}
    }
};

var updatePage = function() {
    for (var x = 0; x < 7; x++) {
	var arrows = document.getElementById(x).children;
	var upArrow = arrows[0];
	var downArrow = arrows[1];
	if (escalators[x][0])
	    upArrow.src = upOn
	else
	    upArrow.src = upOff
	if (escalators[x][1])
	    downArrow.src = downOn
	else
	    downArrow.src = downOff
    }
};

var reloadPage = function() {
    reloadData();
    updatePage();
};

var loadPage = function() {
    loadData();
    updatePage();
};

window.onload = loadPage();
var update = setInterval(reloadPage,1000);