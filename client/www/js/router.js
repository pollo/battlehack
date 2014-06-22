define([
  "app",
  "views/welcome",
  "views/main",
  "views/login",
  "views/selectPack",
  "views/selectPlayer"
], function (app) {
  var Router = Backbone.Router.extend({
    routes: {
      "welcome": "welcome",
      "main": "main",
      "login": "login",
      "selectPack": "selectPack",
      "selectPlayer": "selectPlayer"
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
    },

    selectPlayer: function() {
      var view = new app.SelectPlayerView();
      view.render();
    }
  });

  return Router;
});
