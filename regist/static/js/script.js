var modal = {

    show: function() {
        $('#modal_form').show();
    },

    hide: function() {
        $('#modal_form').hide(); //document.getElementById('modal_form').style.display = 'none';
    },

    setTitle: function(a) {
        $('#modal_form .modal-title').html(a);
    },
    setBody: function(a) {
        $('#modal_form .modal-body').html(a);
    }
};

$(document).ready(function() {
    $('#modal_form').on('click', '[data-dismiss=modal]', function() {
        modal.hide();
    });
});

var hid = function(id) {
    document.getElementById(id).style.display = 'none';
};


//$(document).on('click', '#overlay', modal.hide);

/*var modal2 = {
    show: function() {},
    hide: function() {}
};*/

function btn_click(t) {
    var r = getRandomInt(50, 255);
    var g = getRandomInt(50, 255);
    var b = getRandomInt(50, 255);
    var color = rgbToHex(r, g, b);
    $('body').css('background', color);
    if ((r > 120) && (g > 120) && (b > 120)) {
        $(t).removeClass('btn-default').addClass('btn-primary');
    } else {
        $(t).removeClass('btn-primary').addClass('btn-default');
    }
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function rgbToHex(r, g, b) {
    return "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
}
