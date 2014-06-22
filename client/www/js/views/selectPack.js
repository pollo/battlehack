define([
  "app",
  "text!templates/selectPack.html",
], function (app, template) {
  app.SelectPackView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {
      "click .pack-link": "packSelected"
    },

    render: function () {
      $.ui.setTitle("Select question pack");
      $.ui.updatePanel(this.selector, _.template(template, {packs: app.packs.toJSON()}));
      return this;
    },

    packSelected: function (evt) {
      var $target = $(evt.currentTarget);
      var packid = $target.data('packid');
      app.currentGame.packid = packid;
      app.router.navigate("selectPlayer", {trigger: true});
    }
  });
});
