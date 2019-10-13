

const images = document.getElementsByTagName('img');
// var pars = $("p");
// text = pars[0].innerHTML;
var arrOfStrings = [];
for(var i = 0; i < images.length; i++) {
  $.ajax({
    type: "POST",
    url: "/Users/butterchicken/desktop/dubhacks19/mathread.py",
    data: { param: images[i].src},
    success: function() {
      console.log("something");
      //function call comes here on images[i].src
      //run_quickstart(images[i].src);
      var myAudio = new Audio('/Users/butterchicken/desktop/dubhacks19/output.mp3');
      myAudio.play();
    }
  });
}

// }).done(function( o ) {
   // finds all img tags in the page, store them into an array

//
console.log(arrOfStrings);

//const text = re.query.message \\ req.body.message\\'';




// this potentially could be removed
chrome.runtime.sendMessage({
  url: window.location.href,
  count: images.length
})
