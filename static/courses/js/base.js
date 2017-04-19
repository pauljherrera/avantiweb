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

	function showMenu() {
		$('aside').show(200);
		$('#blank-space').show(200);
		$('aside').removeClass('hidden');
		$('#blank-space').removeClass('hidden');
		$(document.body).trigger("sticky_kit:recalc");
	};

	function hideMenu() {
		$('#blank-space').hide(200);
		$('aside').hide(200);
		$('aside').addClass('hidden');
		$('#blank-space').addClass('hidden');
		$(document.body).trigger("sticky_kit:recalc");
	};

	$('#menu').click(function(event){
		if ($('aside').hasClass('hidden')){
			showMenu();
		} else {
			hideMenu();
		}
	});

	$('#menu-menuicon').click(function(event){
		if ($('aside').hasClass('hidden')){
			showMenu();
		} else {
			hideMenu();
		}
	});

	var mediaquery = window.matchMedia("(max-width: 725px)");
	function handleOrientationChange(mediaquery) {
	  	if (mediaquery.matches) {
	   		hideMenu();
	  	} else {
	  		showMenu();
	  	};
	};
	mediaquery.addListener(handleOrientationChange);

	if (mediaquery.matches) {
	   	hideMenu();
	}
});