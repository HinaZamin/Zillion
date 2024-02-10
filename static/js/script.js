
 /* FadeIn Scroll */
$(document).ready(function() {
    
    /* Every time the window is scrolled ... */
    $(window).scroll( function(){
    
        /* Check the location of each desired element */
        $('.fade').each( function(){
            
            var bottom_of_object = $(this).position().top + $(this).outerHeight();
            var bottom_of_window = $(window).scrollTop() + $(window).height();
            
            /* If the object is completely visible in the window, fade it it */
            if( bottom_of_window > bottom_of_object ){
                
                $(this).animate({'opacity':'0.9'},900);
                    
            }
            
        }); 
    
    });
    
});

$( function() {
  $( "#slider-vertical" ).slider({
    orientation: "vertical",
    range: "min",
    min: 0,
    max: 100,
    value: 60,
    slide: function( event, ui ) {
      $( "#amount" ).val( ui.value );
    }
  });
  $( "#amount" ).val( $( "#slider-vertical" ).slider( "value" ) );
} );