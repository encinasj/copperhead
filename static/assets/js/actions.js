//++======================================Feed articles
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
	var SaveForm = function(){
        var parameters = new FormData(this); 
		var form = $(this);
		$.ajax({
			url: form.attr('data-url'),
			data: parameters,
			type: form.attr('method'),
			dataType: 'json',
			processData: false,
            contentType: false,
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
$('#modal-action').on("submit",".article-update-form",SaveForm)
//delete
$('#all-table').on("click",".show-form-delete",ShowForm);
$('#modal-action').on("submit",".delete-form",SaveForm)
//details
$('#all-table').on("click",".show-details",ShowForm);
$('#modal-action').on("submit",".article-details")
});
//++======================================Category
$(document).ready(function(){
	var ShowFormu = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url-cat"),
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
			url: form.attr('data-url-cat'),
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
//++======================================Brand
$(document).ready(function(){
	var ShowFormb = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url-b"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-b').modal('show');
			},
			success: function(data){
				$('#modal-b .modal-content').html(data.html_form);
			}
		});
	};
	var Saveb = function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url-b'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#tableB ul').html(data.feedc);
					$('#modal-b').modal('hide');
				} else {
					$('#modal-b .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}
//create
$(".Brand-form").click(ShowFormb);
$("#modal-b").on("submit",".create-b",Saveb);
//delete
$('#tableB').on("click",".b-delete",ShowFormb);
$('#modal-b').on("submit",".delete-formb",Saveb)
});
//++======================================Supplier
$(document).ready(function(){
	var ShowFormsp = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url-s"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-s').modal('show');
			},
			success: function(data){
				$('#modal-s .modal-content').html(data.html_form);
			}
		});
	};
	var Savesp = function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url-s'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',
			success: function(data){
				if(data.form_is_valid){
					$('#table-s ul').html(data.feed_s);
					$('#modal-s').modal('hide');
				} else {
					$('#modal-s .modal-content').html(data.html_form)
				}
			}
		})
		return false;
	}
//create
$(".supplier-form").click(ShowFormsp);
$("#modal-s").on("submit",".create-s",Savesp);
//update
$('#table-s').on("click",".show-update-s",ShowFormsp);
$('#modal-s').on("submit",".update-form-s",Savesp)
//delete
$('#table-s').on("click",".delete-s",ShowFormsp);
$('#modal-s').on("submit",".delete-form-s",Savesp)
});
//++======================================
function goBack() {
	window.history.back()
}
//================PDF========================PDF
$(document).ready(function(){
	var ShowFormpdf = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url-pdf"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-action-pdf').modal('show');
			},
			success: function(data){
				$('#modal-action-pdf .modal-content').html(data.html_form);
			}
		});
	};
	var Savepdf = function(){
        var parameters = new FormData(this); 
		var form = $(this);
		$.ajax({
			url: form.attr('data-url-pdf'),
			data: parameters,
			type: form.attr('method'),
			dataType: 'json',
			processData: false,
            contentType: false,
			success: function(data){
				if(data.form_is_valid){
					$('#table-pdf ul').html(data.areas_mb);
					$('#modal-action-pdf').modal('hide');
					$( "#uploadpdf" ).load(window.location.href + " #uploadpdf");
				} else {
					$('#modal-action-pdf .modal-content').html(data.html_form)
				}
			} 
		})
		return false;
	}
//create
$(".pdf-form").click(ShowFormpdf);
$("#modal-action-pdf").on("submit",".create-pdf",Savepdf);
//delete
$('#table-pdf').on("click",".delete-pdf",ShowFormpdf);
$('#modal-action-pdf').on("submit",".delete-formpdf",Savepdf)
});

//================Coment========================Comment
$(document).ready(function(){
	var ShowFormComment = function(){
		var btn = $(this);
		$.ajax({
			url: btn.attr("data-url-comment"),
			type: 'get',
			dataType:'json',
			beforeSend: function(){
				$('#modal-action-comment').modal('show');
			},
			success: function(data){
				$('#modal-action-comment .modal-content').html(data.html_form);
			}
		});
	};
	var SaveComment = function(){
		var form = $(this);
		$.ajax({
			url: form.attr('data-url-comment'),
			data: form.serialize(),
			type: form.attr('method'),
			dataType: 'json',	
			success: function(data){
				if(data.form_is_valid){
					$('#table-comment ul').html(data.areas_mb);
					$('#modal-action-comment').modal('hide');
					$( "#add_comment" ).load(window.location.href + " #add_comment");
				} else {
					$('#modal-action-comment .modal-content').html(data.html_form)
				}
			} 
		})
		return false;
	}

//Create
$(".comment-form").click(ShowFormComment);
$("#modal-action-comment").on("submit",".create-comment",SaveComment);

//Update
$('#table-comment').on("click",".update-comment",ShowFormComment);
$('#modal-action-comment').on("submit",".update-comment",SaveComment)

//delete
$('#table-comment').on("click",".delete-comment",ShowFormComment);
$('#modal-action-comment').on("submit",".delete-comment",SaveComment)
});