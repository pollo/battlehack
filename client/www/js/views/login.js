define([
  "app",
  "models/settings",
], function (app) {
  app.LoginView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {
    },

    render: function () {
      $.ui.setTitle("Logging in...");
      $.ui.updatePanel(this.selector, "Loading...");

      var user = app.settings.where({key: "username"});
      var pass = app.settings.where({key: "password"});

      $.post(SERVER_URL + "/login/", {username: user[0].get("value"), password: pass[0].get("value")})
        .done(function () {
          app.router.navigate("main", {trigger: true});
        });
      return this;
    }
  });
});
