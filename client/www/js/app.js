define(function () {
  var app = {
    root: "welcome",
    storage: openDatabase('appdb', '', 'App data', 5 * 1024 * 1024),
    currentGame: {}
  };
  return app;
});
