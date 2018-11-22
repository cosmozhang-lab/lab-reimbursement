require(["jquery", "vue"], function($, Vue) {
    var vue = new Vue({
        el: "#app",
        data: {
            form: {
                username: "",
                password: ""
            }
        },
        methods: {
            doLogin: function() {
                var username = this.form.username;
                var password = this.form.password;
                if (username.length == 0 || password.length == 0) return;
                status_loading(true);
                $.ajax({
                    url: '/api/login/login',
                    type: 'POST',
                    data: JSON.stringify({ username: username, password: password })
                })
                .done(function(data) {
                    if (data.success) {
                        save_login(username, password);
                        var returnpath = window.location.query.return;
                        if (returnpath) returnpath = unescape(returnpath);
                        window.location.href = returnpath || "/";
                    } else {
                        messagebox("Login", "Login failed. Because: " + data.reason);
                    }
                })
                .fail(function() {
                })
                .always(function() {
                    status_loading(false);
                });
            },
            toRegister: function() {
                var url = "/register";
                if (window.location.query.return) url += "?return=" + window.location.query.return;
                window.location.href = url;
            }
        },
        created: function () {
            var authinfo = get_authinfo();
            if (authinfo) {
                this.form.username = authinfo.username;
                this.form.password = authinfo.password;
            }
            status_loading(false);
        }
    });
});