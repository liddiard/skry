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
        console.log(response);
        // featured image
        $('article .featured-image img').prop('src', response.featured_image.url);
        $('article .featured-image figcaption').html(response.featured_image.caption);
        $('article .featured-image .credit .name').html(response.featured_image.credit);
        if (response.featured_image.courtesy)
            $('article .featured-image .courtesy').html('Courtesy of ');
        if (response.featured_image.organization)
            $('article .featured-image .organization').html(' / '+response.featured_image.organization);
        // article content
        $('article .title').html(response.title);
        $('article .subhead').html(response.subhead);
        if (response.author)
            $('article .author').html('By ' + response.author);
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
