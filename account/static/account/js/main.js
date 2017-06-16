$(document).ready(function(){
	var headerHeight = document.getElementsByTagName('header')[0].offsetHeight;
	var viewable = $(document).scrollTop() + window.innerHeight - 200;
	var chartViewFlag = $('.screen-bottom .screen-left')[0].offsetTop < viewable ? true : false;
	
	window.addEventListener('scroll', function() {
		viewable = $(document).scrollTop() + window.innerHeight - 200;

		$('.to-right').each(function() {
			if (this.offsetTop < viewable) {
				$(this).animate({left: '0'}, 450);
			}
		});

		$('.to-left').each(function() {
			if (this.offsetTop < viewable) {
				$(this).animate({right: '0'}, 550);
			}
		});

		if (!chartViewFlag){
			chart.update();
			chartViewFlag = true;
		}
		
	});

	$('#free-strategy').click(function() {
		var screenOffset = document.getElementById('second-screen').offsetTop;

		if (document.getElementById('blank-space').offsetHeight === 0) {
			headerHeight = 0;
		}

		$('html, body').animate({
	        scrollTop: screenOffset - headerHeight
	    }, 300, 'swing');
	});
	$('#expert-advisor').click(function() {
		var screenOffset = document.getElementById('third-screen').offsetTop;

		if (document.getElementById('blank-space').offsetHeight === 0) {
			headerHeight = 0;
		}

		$('html, body').animate({
	        scrollTop: screenOffset - headerHeight
	    }, 500, 'swing');
	});
	$('#complete-portfolio').click(function() {
		var screenOffset = document.getElementById('fourth-screen').offsetTop;

		if (document.getElementById('blank-space').offsetHeight === 0) {
			headerHeight = 0;
		}

		$('html, body').animate({
	        scrollTop: screenOffset - headerHeight
	    }, 700, 'swing');
	});

	$(window).on('resize', function() {
	  var win = $(this);
	  if (win.width() < 400) {
	    $('.ct-chart').removeClass('ct-major-third');
	    $('.ct-chart').addClass('ct-square');
	  } else {
	  	$('.ct-chart').removeClass('ct-square');
	    $('.ct-chart').addClass('ct-major-third');
	  }
	});

	//Chartist charts.
	var chart01 = new Chartist.Line('#chart01', {
		  labels: ['', '', '', '\'10', '', '', '', '', '', '', '', '', '', '', '', '\'11', '', '', '', '', '', '', '', '', '', '', '', '\'12', '', '', '', '', '', '', '', '', '', '', '', '\'13', '', '', '', '', '', '', '', '', '', '', '', '\'14', '', '', '', '', '', '', '', '', '', '', '', '\'15', '', '', '', '', '', '', '', '', '', '', '', '\'16', '', '', '', '', '', '', '', '', '', '', '\'17'],
		  series: [
		    [-48.0, 1775.0, 1498.0, 1494.0, 1217.0, 899.0, 1231.0, 2004.0, 2324.0, 2138.0, 2074.0, 2326.0, 2102.0, 2427.0, 2528.0, 2702.0, 2820.0, 3956.0, 3918.0, 3751.0, 3940.0, 3603.0, 2786.0, 3349.0, 3782.0, 3781.0, 4060.0, 3590.0, 3644.0, 5157.0, 5386.0, 5416.0, 5980.0, 7081.0, 7112.0, 7176.0, 6811.0, 6877.0, 6711.0, 6548.0, 6671.0, 6990.0, 7102.0, 7289.0, 7128.0, 6911.0, 6798.0, 6853.0, 6898.0, 6824.0, 7157.0, 7545.0, 7962.0, 8357.0, 8711.0, 8260.0, 8698.0, 8474.0, 8635.0, 8777.0, 8845.0, 8537.0, 8305.0, 8253.0, 8267.0, 8527.0, 8644.0, 8586.0, 8793.0, 9041.0, 9559.0, 9624.0, 10134.0, 10710.0, 10591.0, 10892.0, 10635.0, 10501.0, 10753.0, 10650.0, 11037.0, 11381.0, 11088.0, 10900.0, 11228.0, 11377.0, 11949.0, 11442.0, 11638.0, 12030.0, 11865.0, 11816.0, 11764.0, 11769.0, 12180.0, 12086.0, 12296.0],
		  ]
		}, {
		    low: 0,
		    high: 12500,
		    chartPadding: {
				top: 60,
				right: 0,
				bottom: 13,
				left: 15
			},
			showArea: false,
		});

	var chart02 = new Chartist.Line('#chart02', {
		  labels: ['', '', '', '\'10', '', '', '', '', '', '', '', '', '', '', '', '\'11', '', '', '', '', '', '', '', '', '', '', '', '\'12', '', '', '', '', '', '', '', '', '', '', '', '\'13', '', '', '', '', '', '', '', '', '', '', '', '\'14', '', '', '', '', '', '', '', '', '', '', '', '\'15', '', '', '', '', '', '', '', '', '', '', '', '\'16', '', '', '', '', '', '', '', '', '', '', '\'17'],
		  series: [
		    [33.0, 224.0, 206.0, 131.0, 424.0, 512.0, 447.0, 457.0, 425.0, 202.0, 94.0, 16.0, -40.0, -99.0, 16.0, -74.0, -116.0, -17.0, -11.0, -166.0, -99.0, -48.0, -25.0, 213.0, 133.0, 366.0, 689.0, 849.0, 848.0, 720.0, 789.0, 599.0, 496.0, 423.0, 483.0, 495.0, 554.0, 526.0, 562.0, 560.0, 539.0, 540.0, 438.0, 548.0, 579.0, 625.0, 616.0, 640.0, 561.0, 599.0, 674.0, 687.0, 786.0, 705.0, 795.0, 818.0, 530.0, 468.0, 504.0, 465.0, 706.0, 752.0, 831.0, 1017.0, 1060.0, 1303.0, 1430.0, 1645.0, 1849.0, 1699.0, 1832.0, 1747.0, 1538.0, 1639.0, 1523.0, 1880.0, 2017.0, 1843.0, 1731.0, 1628.0, 1415.0, 1681.0, 1685.0, 1818.0, 1851.0, 1734.0, 1848.0, 1787.0, 1739.0, 1951.0, 1902.0, 1993.0],
		  ]
		}, {
		    low: 0,
		    chartPadding: {
				top: 60,
				right: 15,
				bottom: 13,
				left: 15
			},
			showArea: false,
		});

	var chart03 = new Chartist.Line('#chart03', {
		  labels: ['', '', '', '\'10', '', '', '', '', '', '', '', '', '', '', '', '\'11', '', '', '', '', '', '', '', '', '', '', '', '\'12', '', '', '', '', '', '', '', '', '', '', '', '\'13', '', '', '', '', '', '', '', '', '', '', '', '\'14', '', '', '', '', '', '', '', '', '', '', '', '\'15', '', '', '', '', '', '', '', '', '', '', '', '\'16', '', '', '', '', '', '', '', '', '', '', '\'17'],
		  series: [
		    [-48.0, 1775.0, 1498.0, 1494.0, 1217.0, 899.0, 1231.0, 2004.0, 2324.0, 2138.0, 2074.0, 2326.0, 2102.0, 2427.0, 2528.0, 2702.0, 2820.0, 3956.0, 3918.0, 3751.0, 3940.0, 3603.0, 2786.0, 3349.0, 3782.0, 3781.0, 4060.0, 3590.0, 3644.0, 5157.0, 5386.0, 5416.0, 5980.0, 7081.0, 7112.0, 7176.0, 6811.0, 6877.0, 6711.0, 6548.0, 6671.0, 6990.0, 7102.0, 7289.0, 7128.0, 6911.0, 6798.0, 6853.0, 6898.0, 6824.0, 7157.0, 7545.0, 7962.0, 8357.0, 8711.0, 8260.0, 8698.0, 8474.0, 8635.0, 8777.0, 8845.0, 8537.0, 8305.0, 8253.0, 8267.0, 8527.0, 8644.0, 8586.0, 8793.0, 9041.0, 9559.0, 9624.0, 10134.0, 10710.0, 10591.0, 10892.0, 10635.0, 10501.0, 10753.0, 10650.0, 11037.0, 11381.0, 11088.0, 10900.0, 11228.0, 11377.0, 11949.0, 11442.0, 11638.0, 12030.0, 11865.0, 11816.0, 11764.0, 11769.0, 12180.0, 12086.0, 12296.0],
		  ]
		}, {
		    low: 0,
		    high: 12500,
		    chartPadding: {
				top: 60,
				right: 15,
				bottom: 13,
				left: 15
			},
			showArea: false,
		});

	var charts = [chart01, chart02, chart03]

	var seq = 0, delays = 28, durations = 1400;
	chart01.on('created', function() {
  		seq = 0;
	});

	chart01.on('draw', function(data) {
  		seq++;

	  if(data.type === 'line') {
	    // If the drawn element is a line we do a simple opacity fade in. This could also be achieved using CSS3 animations.
	    data.element.animate({
	      opacity: {
	        // The delay when we like to start the animation
	        begin: seq * delays - delays * 185,
	        // Duration of the animation
	        dur: durations,
	        // The value where the animation should start
	        from: 0,
	        // The value where it should end
	        to: 1
	      }
	    });
	  } else if (data.type === 'point') {
		data.element.animate({
		  opacity: {
		    begin: seq * delays - delays * 200,
		    dur: durations,
		    from: 0,
		    to: 1,
		    easing: 'easeOutQuart'
		  }
	    });
	  } 
	});
});
