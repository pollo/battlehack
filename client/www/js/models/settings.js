define([
  "app"
], function (app) {
  var SettingModel = Backbone.Model.extend({
    defaults: {},
    initialize: function () {}
  });

  var SettingCollection = Backbone.Collection.extend({
    model: SettingModel,
    store: new WebSQLStore(app.storage, "settings"),
    comparator: 'key'
  });

  app.SettingCollection = SettingCollection;
  app.SettingModel = SettingModel;

  app.settings = new SettingCollection;
});
