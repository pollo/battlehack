define([
  "app",
  "text!templates/selectPack.html",
], function (app, template) {
  app.SelectPackView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {},

    render: function () {
      $.ui.setTitle("Select question pack");
      $.ui.updatePanel(this.selector, _.template(template, {packs: app.packs.toJSON()}));
      return this;
    }
  });
});
