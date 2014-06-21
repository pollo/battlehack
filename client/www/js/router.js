define([
  "app",
  "views/welcome"
], function (app) {
  var Router = Backbone.Router.extend({
    routes: {
      "welcome": "welcome"
    },

    welcome: function() {
      var view = new app.WelcomeView();
      view.render();
    }
  });

  return Router;
});
