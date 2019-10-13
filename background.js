// calls popup.html/js for testing
window.equations = {}
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  window.equations[request.url] = request.count
})

chrome.browserAction.onClicked.addListener(function (tab) {
  chrome.tabs.create({url: 'popup.html'})
}  )