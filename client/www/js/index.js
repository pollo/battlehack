require.config({
  paths: {
    text: "../bower_components/requirejs-text/text"
  }
});

var init = function() {
  require([
    "app",
    "router"
  ], function (app, Router) {
      app.router = new Router();
      Backbone.history.start();
      app.router.navigate(app.root, {trigger: true});
  });
};

init();
//document.addEventListener('deviceready', init, false);
