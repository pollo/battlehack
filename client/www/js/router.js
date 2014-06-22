define([
  "app",
  "views/welcome",
  "views/main",
  "views/login",
  "views/selectPack"
], function (app) {
  var Router = Backbone.Router.extend({
    routes: {
      "welcome": "welcome",
      "main": "main",
      "login": "login",
      "selectPack": "selectPack"
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
    },

    selectPack: function() {
      var view = new app.SelectPackView();
      view.render();
    }
  });

  return Router;
});
