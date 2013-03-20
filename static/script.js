$(document).ready(function(){
    $('#output_tab').hide();
    $('.panel').click(function(){
        $('#output_tab').slideDown('slow');
    });

    //$('.panel').accordion({collapsible: true, active: false});
});
