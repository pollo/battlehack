define([
  "app",
  "text!templates/selectPlayer.html",
], function (app, template) {
  app.SelectPlayerView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {},

    render: function () {
      var that = this;
      $.ui.setTitle("Select opponent");
      $.ui.updatePanel(this.selector, "Loading...");
      $.get(SERVER_URL + "/users/")
        .done(function (data) {
          $.ui.updatePanel(that.selector, _.template(template, {users: data}));
        });
      return this;
    }
  });
});
