const nav_links = document.getElementsByClassName("nav-link");

for (let i = 0; i < nav_links.length; i++) {
    nav_links[i].addEventListener("click", activate);
}

function activate() {
    this.classList.add("active")
}

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