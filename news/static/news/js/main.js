$(document).ready(function(){
    if (history.pushState) {
        $('.card').click(function(event){
            event.preventDefault();
            $('article, #mask').show();
            showArticle($(this).attr('data-id'));
        });
    }
    $('#mask').click(function(){
        $('article, #mask').hide();
    });
});


function showArticle(id) {
    console.log(id);
    ajaxGet({id: id}, '/api/get_article_by_id/', function(response){
        console.log(response)
        $('article').html(response.body);
        $('article').jScrollPane();
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
