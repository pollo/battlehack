define([
  "app",
  "text!templates/welcome.html",
  "models/settings",
], function (app, template) {
  app.WelcomeView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",
    inProgress: false,

    events: {
      "click #do-signup": "signup"
    },

    render: function () {
      $.ui.setTitle("Welcome");
      $.ui.updatePanel(this.selector, template);
      return this;
    },

    signup: function () {
      if (this.inProgress)
        return;
      var $el = $(this.el);
      var userName = $el.find('#username').val();
      var button = $el.find('#do-submit');
      var oldTxt = button.text();
      button.text("Loading...");
      this.inProgress = true;
      $.post(SERVER_URL + "/users/", {username: userName})
        .done(function (data) {
          app.settings.add([{key: "username", value: userName}, {key: "password", value: data.password}], {merge: true});
          app.settings.each(function(e) { e.save() });
          app.router.navigate("login", {trigger: true});
        })
        .fail(function (xhr) {
          alert(xhr.responseText);
          button.text(oldTxt);
          this.inProgress = false;
        });
    }
  });
});
