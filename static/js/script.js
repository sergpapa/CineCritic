const nav_links = document.getElementsByClassName("nav-link");

$(document).ready(function() {
    const currentPageURL = window.location.href.toLowerCase();
    let home_page = true;
    for (let link of nav_links) {
        const linkID = link.id.toLowerCase();
        if (currentPageURL.includes(linkID)) {
            $(link).addClass("active");
            home_page = false;
        } else if (currentPageURL.includes("movie") || currentPageURL.includes("review") ) {
            $("#movies_list").addClass("active");
        }
    }
    if (home_page) {
        $("#movies_list").addClass("active");
    }
});


function navResizer() {
    if($(window).width() < 400){
        $("#navbar").width(40);
        $("#nav-big").addClass("d-none");
        $("#sidenav-toggler").removeClass("d-none");
        $("#logo").width(50);
        return;
    } else if ($(window).width() < 576 ) {
        $("#navbar").width(60);
        $("#nav-big").addClass("d-none");
        $("#sidenav-toggler").removeClass("d-none");
        $("#logo").width(70);
        return;
    } else if ($(window).width() < 768 ) {
        $("#navbar").width(100);
        $("#logo").width(90);
    } else if ($(window).width() < 992 ) {
        $("#navbar").width(141);
        $("#logo").width(130);
    }else if ($(window).width() < 1200 ) {
        $("#navbar").width(160);
        $("#logo").width(170);
    } else if ($(window).width() < 1370 ) {
        $("#navbar").width(200);
    } else if ($(window).width() > 1370 ) {
        $("#navbar").width("15%");
    }
    $("#nav-big").removeClass("d-none");
        $("#sidenav-toggler").addClass("d-none");
}

$(document).ready(navResizer);

$(window).on("resize", navResizer);

$("#sidenav-toggler").on("click", function() {
    if ($("#navbar").width() > 100 ) {
        $("#navbar").width(60);
        $("#nav-big").addClass("d-none");
        $("#logo").width(70);
    } else {
        $("#navbar").width(175);
        $("#nav-big").removeClass("d-none");
        $("#logo").width(170);
    }
});

// https://stackoverflow.com/questions/13643417/how-to-validate-pattern-matching-in-textarea
// Yann Brelière

$('#add_review').keyup(validateTextarea);
$('#edit_review').keyup(validateTextarea);

function validateTextarea() {
        var errorMsg = "No special characters, no multiple spaces, 25-500 characters";
        var textarea = this;
        var pattern = new RegExp('^' + $(textarea).attr('pattern') + '$');
        // check each line of text
        $.each($(this).val().split("\n"), function () {
            // check if the line matches the pattern
            var hasError = !this.match(pattern);
            if (typeof textarea.setCustomValidity === 'function') {
                textarea.setCustomValidity(hasError ? errorMsg : '');
            } else {
                // Not supported by the browser, fallback to manual error display...
                $(textarea).toggleClass('error', !!hasError);
                $(textarea).toggleClass('ok', !hasError);
                if (hasError) {
                    $(textarea).attr('title', errorMsg);
                } else {
                    $(textarea).removeAttr('title');
                }
            }
            return !hasError;
        });
    }
