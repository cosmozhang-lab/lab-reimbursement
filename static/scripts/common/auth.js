define(function() {
    var defined = {};
    defined.save_login = function(username, password) {
        window.localStorage["auth"] = username + ":" + password;
    };
    defined.clear_login = function() {
        window.localStorage.removeItem("auth");
    };
    defined.get_authstr = function() {
        return window.localStorage["auth"];
    };
    defined.get_authinfo = function() {
        var authstr = window.localStorage["auth"];
        if (authstr) {
            authstr = authstr.split(":");
            return {
                username: authstr[0],
                password: authstr[1]
            };
        } else {
            return undefined;
        }
    };
    return defined;
});