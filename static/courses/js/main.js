$(document).ready(function(){
	$('.single-module').click(function(event){
		// Data sent with ajax. Needed to retrieve the template.
		var send_data = { course : $(this).data('course'),
						  module : $(this).data('module')};		

		// Changes the title.
		$('#module-title').fadeOut(function() {
			$('#module-title').html($(this).children().html().trim());
        	$('#module-title').fadeIn();
        }.bind(this));

		// Fades the content out, and only then makes the ajax call.
		$('content').fadeOut(function() {
			$.ajax({
	            url: "{% url 'courses:get_content' %}",
	            type: "GET",
	            data: send_data
        	}).done(function(data){
        		// Appends and shows the retrieved page.
        		$('content').children().remove();
				$('content').append(data);
				$('content').fadeIn();
        	});
		});	      
	});
});