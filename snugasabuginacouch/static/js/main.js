$(document).ready(function(){
    $('#query-form').on('submit', function(event){
        event.preventDefault();
        query_post();
    })
});
$(document).on('click', '.image-checkbox', function (event) {
      $(this).toggleClass('image-checkbox-checked');
      var $checkbox = $(this).find('input[type="checkbox"]');
      $checkbox.prop("checked",!$checkbox.prop("checked"))

      event.preventDefault();
});

function query_post() {
    $.ajax({
        url : list_manager.URLS.search,
        type : "POST", 
        data : { post_query : $('#query-search').val(),
                 filters_choices: $('#filters-choices').val(),
         }, 
        success : function(json) {
            $('#query-search').val(''); // remove the value from the input
            $.each(json, function(key, value) {
                $("#movies-choices").prepend(
                    "<option value=" + value.id + ">" + value.title + "</option>"
                );
                $("#thumbnail-img-movies-choices").prepend(
                    "<div class='col-xs-4 col-sm-3 col-md-2 nopad text-center'> " +
                    "<label class='image-checkbox'> " + 
                    "<img src='" + (value.poster_url != '' ? value.poster_url : list_manager.URLS.default_poster) + "' " +
                    "alt='"+ value.title + "' class='img-responsive'/><input type='checkbox' name=image[] id='" + value.id + "' " +
                    "value=''/> <i class='fa fa-check hidden'></i></label></div>"
                );
            })
            // image gallery
            // init the state from the input
            $('.image-checkbox').each(function () {
              if ($(this).find('input[type="checkbox"]').first().attr("checked")) {
                $(this).addClass('image-checkbox-checked');
              }
              else {
                $(this).removeClass('image-checkbox-checked');
              }
            })            
        },
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! Error: " + xhr.responseJSON.err +
                " <a href='" + list_manager.URLS.search + "' class='close'>&times;</a></div>"); 
        }
    });
};

$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});
