$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
        theme: "minimal"
    });

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar, #content').toggleClass('active');
        $('.collapse.in').toggleClass('in');
        $('a[aria-expanded=true]').attr('aria-expanded', 'false');
    });
});

$('#meuModal').on('shown.bs.modal', function () {
    $('#meuInput').trigger('focus')
});

$('#datepicker-datainicio').datepicker({
    uiLibrary: 'bootstrap4'
});

$('#datepicker-datafim').datepicker({
    uiLibrary: 'bootstrap4'
});