$(document).ready(function(){
    if (window.context.article) setUpArticle();
    if (history.pushState) {
        $('.card').click(function(event){
            event.preventDefault();
            history.pushState({}, null, $(this).attr('href'));
            $('article, #mask').show();
            window.originalScrollY = window.scrollY;
            $('#wrap').css({position: 'fixed', top: -window.originalScrollY})
            showArticle($(this).attr('data-id'));
        });
    }
    $('#mask').click(function(event){
        if (history.pushState) {
            event.preventDefault();
            history.pushState({}, null, '/');
            $('article, #mask').hide();
            clearArticle();
            $('#wrap').css({position: '', top: ''})
            $(document).scrollTop(window.originalScrollY);
        }
    });
    shapeshiftCards();
    $(window).on('resize', function(){
        resizeCards();
    });
});

function resizeCards() {
    var width = $('.cards').width();
    var card_unit = 310;
    var rearrange_needed = false;
    $('.card').each(function(){
        var colspan_current = $(this).attr('data-ss-colspan');
        var colspan_original = $(this).attr('data-ss-original-colspan');
        if (colspan_current*card_unit >= width) {
            $(this).attr('data-ss-colspan', Math.floor(width/card_unit)-1);
            rearrange_needed = true;
        }
        else if (colspan_current != colspan_original && width-card_unit >= colspan_original*card_unit) {
            $(this).attr('data-ss-colspan', colspan_original);
            rearrange_needed = true;
        }
    });
    if (rearrange_needed) {
        window.setTimeout(shapeshiftCards, 500); // TODO: Fix. Magic number delay shouldn't be necessary but is for layout to function properly.
    }
}

function showArticle(id) {
    ajaxGet({id: id}, '/api/get_article_by_id/', function(response){
        console.log(response);
        // infobar
        $('article').html(response.html);
        setUpArticle();
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

function shapeshiftCards() {
    var widest_card = 1;
    $('.card').each(function(){
        var colspan = $(this).attr('data-ss-colspan');
        if (colspan > widest_card)
            widest_card = colspan;
    });
    $('.cards').shapeshift({gutterX: 10, gutterY: 10, paddingX: 0, paddingY: 0, minColumns: widest_card, animated: false});
}

function setUpArticle() {
    var FB_SHARE_URL = "https://www.facebook.com/sharer/sharer.php?u=";
    $('article .popup').magnificPopup({type: 'image', closeOnContentClick: true});
    $('article audio').mediaelementplayer({audioWidth: '100%'});
    $('article .body').readingTime('.reading-time');
    $('article .facebook').prop('href', FB_SHARE_URL+document.URL);
    var tweet = $('article .share .twitter').prop('href');
    tweet += (' '+document.URL);
    $('article .share .twitter').prop('href', tweet);
    readingProgressBar();
}

function clearArticle() {
    $('article').empty();
}

function readingProgressBar() {
    // from: http://css-tricks.com/reading-position-indicator/
    var winHeight = $(window).height(), 
    docHeight = $(document).height(),
    progressBar = $('progress'),
    max, value;

    /* Set the max scrollable area */
    max = docHeight - winHeight;
    progressBar.attr('max', max);

    $(document).on('scroll', function(){
        value = $(window).scrollTop();
        progressBar.attr('value', value);
    });

    $('#mask').on('click', function(event){
        $(document).unbind('scroll');
        progressBar.attr('value', 0);
        $(this).unbind(event);
    });
}

(function($) {
    /*!
    A very simplified version of:

    Name: Reading Time
    Dependencies: jQuery
    Author: Michael Lynch
    Author URL: http://michaelynch.com
    Date Created: August 14, 2013
    Date Updated: January 24, 2014
    Licensed under the MIT license

    */
    $.fn.readingTime = function(selector) {

        //return if no element was bound
        //so chained events can continue
        if(!this.length) { 
            return this; 
        }

        //define element
        var el = $(this);

        // words per minute
        var wpm = 270;

        // calculate the reading time
        var reading_time = Math.round(el.text().split(' ').length / wpm);

        // don't display anything if reading time is less that 30 secs
        if (reading_time < 1)
            return this;
        else
            $(selector).html(reading_time + ' min. read &ndash; ');
    }
})(jQuery);
