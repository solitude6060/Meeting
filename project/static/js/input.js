$( ".field" ).hover(
  function() {
      $(this).addClass("field-expanded");
  },
  function() {
    	if($( this ).find( ".text-area" ).val() == ""  && !$(this).find(".text-area").is(':focus')){
    	$(this).removeClass("field-expanded");
      }
  }
)

$( ".field" ).click(function() {
  $(this).addClass("field-expanded");
});

$( ".text-area" ).blur(
  function() {
      if($( this ).val() == "")
        $( this ).parent().removeClass("field-expanded");
  }
);
