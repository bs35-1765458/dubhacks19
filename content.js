
// finds all img tags in the page, store them into an array
const images = document.getElementsByTagName('img'); 
for(var i = 0; i < images.length; i++) {
    //function call comes here on images[i].src
}

// this potentially could be removed
chrome.runtime.sendMessage({
  url: window.location.href,
  count: images.length
})