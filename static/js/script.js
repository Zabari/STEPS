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

// Fetch data from server and update page
var reloadData = function() {
    $.getJSON("/getData", function(data) {
        updatePage(data);
    } );
};

// Given data, update page
var updatePage = function(escalator_status) {
    // Get the escalator names delivered in the data
    var escalator_names = Object.keys(escalator_status);
    var data, _status;
    // For every escalator, run either `setON` or `setOFF`
    for (var escalator_name in escalator_names) {
        data = escalator_status[escalator_name];
        _status = data.status;
        if (_status)
            setON(escalator_name);
        else
            setOFF(escalator_name);

    }
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
  reloadData();
}, 2000);



// SIDEBAR
/* activate sidebar */
$('#sidebar').affix({
  offset: {
    top: 235
  }
});

/* activate scrollspy menu */
var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;

$body.scrollspy({
  target: '#leftCol',
  offset: navHeight
});

/* smooth scrolling sections */
$('a[href*=#]:not([href=#])').click(function() {
  if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
    var target = $(this.hash);
    target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
    if (target.length) {
      $('html,body').animate({
        scrollTop: target.offset().top - 60
      }, 500);
      return false;
    }
  }
});
