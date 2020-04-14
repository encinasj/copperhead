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
//++======================================Category
$(document).ready(function(){
	var ShowFormu = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-cat').modal('show');
			},
			success: function(data){
				$('#modal-cat .modal-content').html(data.html_form);
			}
		});
	};
	var Savecat = function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#tablec ul').html(data.feedc);
					$('#modal-cat').modal('hide');
				} else {
					$('#modal-cat .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}
//create 
$(".category-form").click(ShowFormu);
$("#modal-cat").on("submit",".create-category",Savecat);
//delete
$('#tablec').on("click",".create-category-delete",ShowFormu);
$('#modal-cat').on("submit",".delete-formc",Savecat) 
});

//++======================================Microbusiness
$(document).ready(function(){
	var ShowFormmb = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url-m"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-mb').modal('show');
			},
			success: function(data){
				$('#modal-mb .modal-content').html(data.html_form);
			}
		});
	};
	var Savemb = function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url-m'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#tableM ul').html(data.feedc);
					$('#modal-mb').modal('hide');
				} else {
					$('#modal-mb .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}
//create 
$(".Microb-form").click(ShowFormmb);
$("#modal-mb").on("submit",".create-mb",Savemb);
//delete
$('#tableM').on("click",".mb-delete",ShowFormmb);
$('#modal-mb').on("submit",".delete-formmb",Savemb) 
});