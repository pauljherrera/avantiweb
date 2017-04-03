$(document).ready(function(){
	$('.single-course').click(function(event){
		var nextSibling = $(this).parent().next();;
		var droppedDown = $('.dropped-down');

		if (droppedDown[0] == nextSibling[0]) {
			$(nextSibling).slideUp();
			$(nextSibling).removeClass('dropped-down');
		} else {
			$('.dropped-down').slideUp();
			$('.dropped-down').removeClass('dropped-down');
			$(nextSibling).slideDown();
			$(nextSibling).addClass('dropped-down');
		};
	});

	$('#menu').click(function(event){
		if ($('aside').hasClass('hidden')){
			$('aside').show(200);
			$('#blank-space').show(200);
			$('aside').removeClass('hidden');
			$('#blank-space').removeClass('hidden');
			$(document.body).trigger("sticky_kit:recalc");
		} else {
			$('#blank-space').hide(200);
			$('aside').hide(200);
			$('aside').addClass('hidden');
			$('#blank-space').addClass('hidden');
			$(document.body).trigger("sticky_kit:recalc");
		}
		
		
	});
});