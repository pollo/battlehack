define([
  "app",
  "views/welcome",
  "views/main",
  "views/login"
], function (app) {
  var Router = Backbone.Router.extend({
    routes: {
      "welcome": "welcome",
      "main": "main",
      "login": "login",
    },

    welcome: function() {
      var view = new app.WelcomeView();
      view.render();
    },

    main: function() {
      var view = new app.MainView();
      view.render();
    },

    login: function() {
      var view = new app.LoginView();
      view.render();
    }
  });

  return Router;
});
