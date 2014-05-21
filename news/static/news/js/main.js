$(document).ready(function(){
    if (history.pushState) {
        $('.card').click(function(event){
            event.preventDefault();
            $('article, #mask').show();
            window.originalScrollY = window.scrollY;
            $('#main').css({position: 'fixed', top: -window.originalScrollY})
            showArticle($(this).attr('data-id'));
        });
    }
    $('#mask').click(function(){
        $('article, #mask').hide();
        $('#main').css({position: '', top: ''})
        $(document).scrollTop(window.originalScrollY);
    });
});


function showArticle(id) {
    console.log(id);
    ajaxGet({id: id}, '/api/get_article_by_id/', function(response){
        console.log(response)
        $('article .featured-image').prop('src', response.featured_image);
        $('article .title').html(response.title);
        $('article .subhead').html(response.subhead);
        $('article .author').html(response.author);
        $('article .body').html(response.body);
    });
}

/* utility functions */

function ajaxGet(params, endpoint, callback_success) {
    $.ajax({
        type: "GET",
        url: endpoint,
        data: params,
        crossDomain: true,
        success: callback_success,
        error: function(xhr, textStatus, errorThrown) {
            if (xhr.status != 0)
                console.error('Oh no! Something went wrong. Please report this error: \n'+errorThrown+xhr.status+xhr.responseText);
        }
    }); 
}