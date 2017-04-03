$(document).ready(function(){
	$('.login-button').click(function(event){
		event.preventDefault();
		if ($(this).data('type') == 'login') {
			$('.fill-in01').each(function() {
				$(this).html('Login');
			});
			$('#pop-login').show().css('display', 'flex');
			$('#blur').show();
		} else if ($(this).data('type') == 'sign-up') {
			$('.fill-in01').each(function() {
				$(this).html('Register');
			});
			$('.fill-in02').html('Registering you accept our Terms and Conditions.')
			$('#pop-login').show().css('display', 'flex');
			$('#blur').show();
		}
	});

	$('#blur').click(function(event){
		$('#pop-login').hide();
		$('#blur').hide();
	});

	$('.close').click(function(event){
		$('#pop-login').hide();
		$('#blur').hide();
	});
});