(function($) {

	"use strict";

	$('[data-toggle="tooltip"]').tooltip()

	// $('#exampleModalCenter').modal('show')

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

})(jQuery);

const expirationDateInput = document.getElementById('expiration-date');

expirationDateInput.addEventListener('input', function(e) {
  let input = e.target.value;
  let cleanedInput = input.replace(/[^0-9]/g, '');

  // Format the input as MM/YY
  let formattedInput = cleanedInput.replace(/^(\d{2})\/?(\d{0,2})/, '$1/$2');
  
  // Limit the input to 5 characters
  formattedInput = formattedInput.slice(0, 5);
  
  // Update the input field
  if (input !== formattedInput) {
    e.target.value = formattedInput;
    // Move the cursor to just after the last digit
    e.target.setSelectionRange(formattedInput.length, formattedInput.length);
  }
});

expirationDateInput.addEventListener('keydown', function(e) {
  if (e.key === 'Backspace') {
    let input = e.target.value;
    let cleanedInput = input.replace(/[^0-9]/g, '');

    if (cleanedInput.length > 0) {
      // Remove the last character from the cleaned input
      let newCleanedInput = cleanedInput.slice(0, cleanedInput.length - 1);

      // Format the input as MM/YY
      let formattedInput = newCleanedInput.replace(/^(\d{2})\/?(\d{0,2})/, '$1/$2');

      // Update the input field
      e.target.value = formattedInput;
      // Move the cursor to just after the last digit
      e.target.setSelectionRange(formattedInput.length, formattedInput.length);
    }
  }
});
