window.onload = function () {
    'use strict';
    /* prevent placeholder from sliding on input content */
    var inp = document.getElementsByTagName('input'),
        il = inp.length;

    while(--il) {
        inp[il].addEventListener('blur', function () {
            var t = this;
            (t.value.length > 0) ? t.classList.add('have-content') : t.classList.remove('have-content');
        });
    }

    /* trigger click event on checkbox when click on text */
    var i = 0,
        remember = document.getElementsByClassName("remember-me")[0],
        rememberCB = remember.getElementsByTagName("input")[0],
        rememberTxt = remember.getElementsByClassName("remember-me-txt")[0];
    
    rememberTxt.addEventListener('click', function () {
        i === 0 ? i = 1 : i = 0;
        if (i)
            rememberCB.checked = true;
        else
            rememberCB.checked = false;
    });
};
