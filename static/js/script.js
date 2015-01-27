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


// We track whether the tab is active to decrease update frequency when the user isn't looking
var isTabActive = true;

// http://stackoverflow.com/a/1760283/805556
window.onfocus = function () { 
  isTabActive = true; 
}; 

window.onblur = function () { 
  isTabActive = false; 
};

var timeSinceLastChecked = 0;

// Fetch data from server and update page
var reloadData = function() {
    // If tab isn't currently active, and if we've checked in the last 8 seconds, don't check again
    if (!isTabActive) {
        if (timeSinceLastChecked < 8000) {
            timeSinceLastChecked += UPDATE_FREQUENCY;
            return;
        }
    }

    timeSinceLastChecked = 0;

    $.getJSON("/getData", function(data) {
        updatePage(data);
    } );
};

// Given data, update page
var updatePage = function(escalator_status) {
    // Get the escalator names delivered in the data
    var _status;
    // For every escalator, run either `setON` or `setOFF`
    for (var i = 0; i < escalator_status.length; i++) {
        _status = escalator_status[i];
        if (_status)
            setON(escalators[i]);
        else
            setOFF(escalators[i]);

    }
};

// Simulation Stuff

/**********************************************
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
********************************************/



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
