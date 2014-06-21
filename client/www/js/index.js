require.config({
  paths: {
    text: "../bower_components/requirejs-text/text"
  }
});

var SERVER_URL = "http://192.168.209.125:8000";

var init = function() {
  require([
    "app",
    "router"
  ], function (app, Router) {
      $.ui.launch();
      $.ui.ready(function() {
        $('.app-loading').hide();
        app.router = new Router();
        Backbone.history.start();
        app.router.navigate(app.root, {trigger: true});
      });
  });
};

init();
//window.addEventListener('load', init);
//document.addEventListener('deviceready', init, false);
