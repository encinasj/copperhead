const tim_input = $("#tim-input")
const tim_div = $('#replaceable-content')
const endpoint = '/Buscador/'
const delay_by_in_ms = 700
let scheduled_function = false

let ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			// fade out the tim_div, then:
			tim_div.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				tim_div.html(response['html_from_view'])
				// fade-in the div with new contents
				tim_div.fadeTo('slow', 1)
			})
		})
}

tim_input.on('keyup', function () {
	const request_parameters = {
		q: $(this).val() 
	}
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
