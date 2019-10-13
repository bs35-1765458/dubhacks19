// TESTING:
// pop up that prints number of count of image occurrence
// (could be removed)

document.addEventListener('DOMContentLoaded', function () {

  const bg = chrome.extension.getBackgroundPage()
  Object.keys(bg.equations).forEach(function (url) {
    const div = document.createElement('div')
    div.textContent = `${url}: ${bg.equations[url]}`
    document.body.appendChild(div)
  })

}, false)