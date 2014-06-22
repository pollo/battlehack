require.config({
  paths: {
    text: "../bower_components/requirejs-text/text"
  }
});

var SERVER_URL = "http://192.168.2.106:8000";

var init = function() {
  require([
    "app",
    "router",
    "models/settings"
  ], function (app, Router) {
      $.ui.launch();
      $.ui.ready(function() {
        $('.app-loading').hide();
        app.router = new Router();
        Backbone.history.start();
        app.settings.fetch({success: function() {
          if (app.settings.where({key: "username"}).length > 0) {
            app.router.navigate("login", {trigger: true});
          }
          else {
            app.router.navigate("welcome", {trigger: true});
          }
        }});
      });
  });
};

init();
//window.addEventListener('load', init);
//document.addEventListener('deviceready', init, false);
