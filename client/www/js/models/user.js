define([
  "app",
], function (app, template) {
  app.UserModel = Backbone.Model.extend({
    defaults: {
      userName: "anonymous"
    },
    initialize: function () {
    }
  });
});
