define([
  "app"
], function (app) {
  var QuestionPackModel = Backbone.Model.extend({
    defaults: {id: null, name: null, topics: null},
    initialize: function () {}
  });

  var QuestionPackCollection = Backbone.Collection.extend({
    model: QuestionPackModel,
    comparator: 'id'
  });

  var TopicModel = Backbone.Model.extend({
    defaults: {id: null, name: null},
    initialize: function () {}
  });

  var TopicsCollection = Backbone.Collection.extend({
    model: TopicModel,
    comparator: 'id'
  });

  app.QuestionPackCollection = QuestionPackCollection;
  app.QuestionPackModel = QuestionPackModel;

  app.TopicModel = TopicModel;
  app.TopicsCollection = TopicsCollection;

  app.packs = new QuestionPackCollection;
});
