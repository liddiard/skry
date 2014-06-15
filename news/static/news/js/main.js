$(document).ready(function(){
    // initial setup
    window.originalScrollY = 0;
    shapeshiftCards();
    if (window.context.article) setUpArticle();

    // event bindings
    $(window).on('resize', function(){
        resizeCards();
    });
    if (history.pushState) {
        $('.card').click(function(event){
            showArticle(event, $(this));
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
    $('.cards').on('ss-rearranged', function(event, selected){
        var id = $(selected).attr('data-id');
        var new_position = window.context.first_position - $(selected).index();
        ajaxPost(
            {id: id, new_position: new_position},
            '/api/article/position-change/',
            function(response) { console.log(response) }
        );
    });
    $('nav').hover(
        function(){
            $(this).find('ul').show();
        },
        function(){
            $(this).find('ul').hide();
        }
    );
    $('nav li a').click(function(event){
        event.preventDefault();
        $(this).parent().parent().hide();
        var params = {};
        var $current_category = $('nav .current.category .name');
        if ($current_category.text() === 'All')
            params.start_after = $('.card').last().attr('data-position');
        $current_category.text($(this).attr('data-category'));
        params.quantity = 12;
        params.category = $(this).attr('id');
        addCards(params);
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
        window.setTimeout(shapeshiftCards, 500); // TODO: Fix. Magic number delay shouldn't be necessary for layout to function properly.
    }
}

function showArticle(event, $el) {
    event.preventDefault();
    history.pushState({}, null, $el.attr('href'));
    $('article, #mask').show();
    window.originalScrollY = window.scrollY;
    loadArticle($el.attr('data-id'));
}

function loadArticle(id) {
    ajaxGet({format: 'json'}, '/article/'+id+'/', function(response){
        console.log(response);
        $('article').html(response.html);
        setUpArticle();
    });
}

function addCards(params) {
    var new_cards_retrieved = false;
    if (typeof params.category !== 'undefined') {
        $('.card').not('.'+params.category).fadeOut('fast', function(){ 
            $(this).remove();
            if (!new_cards_retrieved) { 
                // only call getNewCards once in total, not once per selected element
                getNewCards(params);
                new_cards_retrieved = true;
            }
        });
    }
    else
        getNewCards(params);
}

function getNewCards(params) {
    ajaxGet(
        params,
        '/api/article/get-cards/',
        function(response) {
            var cards = response.cards;
            for (var i = 0; i < cards.length; i++) {
                $('.cards').append($.parseHTML(cards[i].html)).css('opacity', 0).animate({opacity: 1}, 250);
                // use opacity animation instead of .hide().fadeIn() because elements need to be 
                // consuming space in the DOM when shapeshift rearrange is called
            }
            $('.card').unbind('click').click(function(event){
                showArticle(event, $(this));
            });
            if (cards.length)
                shapeshiftCards(); // if new cards were added, we need to re-instantiate shapeshift
            else
                $('.cards').trigger('ss-rearrange'); // otherwise, just trigger a rearrange
        }
    );
}


/* utility functions */

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

function ajaxPost(params, endpoint, callback_success) {
    params.csrfmiddlewaretoken = getCookie('csrftoken');
        $.ajax({
        type: "POST",
        url: endpoint,
        data: params,
        success: callback_success,
        error: function(xhr, textStatus, errorThrown) {
            console.log("Oh no! Something went wrong. Please report this error: \n"+errorThrown+xhr.status+xhr.responseText);
        }
    }); 
}

function ajaxGet(params, endpoint, callback_success) {
    $.ajax({
        type: "GET",
        url: endpoint,
        data: params,
        crossDomain: true,
        success: callback_success,
        error: function(xhr, textStatus, errorThrown) {
            console.error('Oh no! Something went wrong. Please report this error: \n'+errorThrown+xhr.status+xhr.responseText);
        }
    }); 
}

function shapeshiftCards(custom_options) {
    var widest_card = 1;
    $('.card').each(function(){
        // find the widest card
        var colspan = $(this).attr('data-ss-colspan');
        if (colspan > widest_card)
            widest_card = colspan;
    });
    var default_options = {gutterX: 10, gutterY: 10, paddingX: 0, paddingY: 0, minColumns: widest_card, animated: true, align: 'left'};
    var options = $.extend({}, default_options, custom_options);
    $('.cards').shapeshift(options);
}

function setUpArticle() {
    var FB_SHARE_URL = "https://www.facebook.com/sharer/sharer.php?u=";
    $('#wrap').css({position: 'fixed', top: -window.originalScrollY})
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
