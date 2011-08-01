var scrollSpeed = 25;
var step = 1;
var current = 0;
var imageWidth = 2247;
var headerWidth = 940;		
var restartPosition = -(imageWidth - headerWidth);


$(document).ready( function(){
	$("#contact_info").hide();
	$("#contact_info_a").click( function(){
		$("#contact_info").slideToggle( "slow");
	});
	
	function scrollBg()
	{
		current -= step;
		if (current == restartPosition)
		{
			current = 0;
		}
		$('#crimescene_banner').css("background-position",current+"px 0");
	}
	var init = setInterval(scrollBg, scrollSpeed);
	
	//img hover stuff
	$("#warrants-img").hover(
	 function()
	 {
	  this.src = this.src.replace("_btn2","_btn1");
	 },
	 function()
	 {
	  this.src = this.src.replace("_btn1","_btn2");
	 }
	);
	//911 img hover stuff
	$("#911-img").hover(
	 function()
	 {
	  this.src = this.src.replace("_btn1","_btn2");
	 },
	 function()
	 {
	  this.src = this.src.replace("_btn2","_btn1");
	 }
	);
	
	//home button hover
	$("#home-img" ).hover(
		function()
		{
			this.src = this.src.replace( "_btn2","_btn1");
		},
		function()
		{
			this.src = this.src.replace( "_btn1","_btn2" );
		}
	);

});