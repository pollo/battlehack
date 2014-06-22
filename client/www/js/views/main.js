define([
  "app",
  "text!templates/main.html",
  "models/settings",
], function (app, template) {
  app.MainView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {},

    render: function () {
      $.ui.setTitle("Main");
      $.ui.updatePanel(this.selector, template);
      $.get(SERVER_URL + "/questions")
        .done(function(data) {

        })
        .fail(function(data) {
          alert(data.error);
        })
      return this;
    }
  });
});
