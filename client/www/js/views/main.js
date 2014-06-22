define([
  "app",
  "text!templates/main.html",
  "models/settings",
], function (app, template) {
  app.MainView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {
      "click #go-start-game": "startGame",
      "click #go-settings": "settings"
    },

    render: function () {
      $.ui.setTitle("Main");
      $.ui.updatePanel(this.selector, template);
      return this;
    },

    startGame: function () {
      app.router.navigate("selectPack", {trigger: true});
    },

    settings: function () {
      alert("Not implemented! :(");
    }
  });
});
