$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

    socket.on('disconnect', function() {
	console.log("dis");
    });
    
    socket.on('connect', function() {
	console.log("con");
	socket.emit('my event', {data: 'I\'m connected!'});
    });
    
    socket.on('update', function(msg) {
	var data = JSON.parse(msg);
	var d = new Date();
	var template = "<div class='col-xs-4'>" +
	  " <div class='panel panel-default' style='height:120px'>" +
	  "   <div class='panel-heading'>" +
          "     <h3 class='panel-title'> Message at " + d.toLocaleTimeString() + "</h3>" +
	  "   </div>" +
	  "   <div class='panel-body'>" + data['message'] + "</div>" +
	  " </div>" +
	  "</div>"

	$(template).prependTo("#container").hide().fadeIn('slow');	
    });

});
