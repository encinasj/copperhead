$(document).ready(function(){
	var ShowForm = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-action').modal('show');
			},
			success: function(data){
				$('#modal-action .modal-content').html(data.html_form);
			}
		});
	};
	var SaveForm =  function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#all-table ul').html(data.feed);
					$('#modal-action').modal('hide');
				} else {
					$('#modal-action .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}
//create 
$(".show-form").click(ShowForm);
$("#modal-action").on("submit",".create-form",SaveForm);
//update
$('#all-table').on("click",".show-form-update",ShowForm);
$('#modal-action').on("submit",".update-form",SaveForm)
//delete
$('#all-table').on("click",".show-form-delete",ShowForm);
$('#modal-action').on("submit",".delete-form",SaveForm) 
});