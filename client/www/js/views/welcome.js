define([
  "app",
  "text!templates/welcome.html",
], function (app, template) {
  app.WelcomeView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {
      "click #do-signup": "signup"
    },

    render: function () {
      $.ui.setTitle("Welcome");
      $.ui.updatePanel(this.selector, template);
      return this;
    },

    signup: function () {
      var userName = $(this.el).find('#username').val();
      $.post(SERVER_URL + "/createuser/", {username: userName}, function (data) {
        console.log(userName);
        app.currentUser = new app.UserModel({userName: userName, password: data.password});
        console.log(app.currentUser);
      })
    }
  });
});
