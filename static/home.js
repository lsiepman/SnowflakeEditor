

showPreviewPage = function(input) {
    var index = input.lastIndexOf("_");
    var result = input.substr(index+1);
    var iframeLoc = "previews/" + result + ".html"
    
    var iframe = document.getElementById('iframe_id');
    iframe.src = iframeLoc
}