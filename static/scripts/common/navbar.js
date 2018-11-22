define(["jquery"], function($) {
    $(function() {
        $("#button-signout").click(function(event) {
            $.ajax({
                url: '/api/login/logout',
                type: 'POST'
            })
            .done(function() {
                window.location.href = "/login";
            })
            .fail(function() {
            })
            .always(function() {
            });
        });
    });
});
