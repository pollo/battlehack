define([
  "app",
  "text!templates/main.html",
  "models/settings",
], function (app, template) {
  app.MainView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {
    },

    render: function () {
      $.ui.setTitle("Main");
      $.ui.updatePanel(this.selector, template);
      return this;
    }
  });
});
