define(["jquery"], function($) {
    function status_loading(on) {
        if (on) $("#cover").fadeIn(100);
        else $("#cover").fadeOut(100);
    }

    $.ajaxSetup({
        contentType: 'application/json',
        beforeSend: function (xhr) {
            var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    function messagebox(title, content) {
        $("#modal-message-title").text(title);
        $("#modal-message-body").text(content);
        $("#modal-message").modal("show");
    }

    window.location.query = (function(url) {
        var querystr = /\?[^#]+/.exec(url);
        if (!querystr) return {};
        querystr = querystr[0].slice(1);
        var queryarr = querystr.split("&");
        var querydict = {};
        for (var i = 0; i < queryarr.length; i++) {
            var queryitem = queryarr[i].split("=");
            querydict[queryitem[0]] = ((queryitem.length > 1) ? queryitem[1] : null);
        }
        return querydict;
    })(window.location.href);

    window.location.uri = (function(url) {
        return /[^\?#]+/.exec(url)[0];
    })(window.location.href);

    function make_url(uri, query) {
        query = query || {};
        var url = uri;
        var qks = Object.keys(query);
        if (qks.length > 0) {
            var querystr = "?" + qks.map(function(k) { return k + "=" + query[k]; }).join("&");
            url += querystr;
        }
        return url;
    }
});