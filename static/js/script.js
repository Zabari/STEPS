var escalators = [
  "up23", "down23",
  "up24", "down24",
  "up35", "down35",
  "up46", "down46",
  "up57", "down57",
  "up68", "down68",
  "up79", "down79",
];

function setON(id) {
  var item = document.getElementById(id);
  var doc = item.getSVGDocument();
  var path = doc.querySelector("path");
  path.setAttribute("fill", "green");
};

function setOFF(id) {
  var item = document.getElementById(id);
  var doc = item.getSVGDocument();
  var path = doc.querySelector("path");
  path.setAttribute("fill", "red");
};

// Simulation Stuff

var getRandomBoolean = function() {
  var randomNumber = Math.random() >= 0.5;
  return randomNumber;
};

function setRandom() {
  for (var item in escalators) {
    // console.log(escalators[item]);
    if (getRandomBoolean()) {
      setON(escalators[item]);
    } else {
      setOFF(escalators[item]);
    };
  };
}

window.setInterval(function(){
  setRandom();
}, 2000);
