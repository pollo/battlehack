define([
  "app",
  "models/settings",
  "models/questions",
], function (app) {
  app.LoginView = Backbone.View.extend({
    selector: "#main-panel",
    el: "#main-panel",

    events: {
    },

    render: function () {
      $.ui.setTitle("Logging in...");
      $.ui.updatePanel(this.selector, "Loading...");

      var user = app.settings.where({key: "username"});
      var pass = app.settings.where({key: "password"});

      $.post(SERVER_URL + "/login/", {username: user[0].get("value"), password: pass[0].get("value")})
        .done(function () {
          app.packs.reset();
          $.get(SERVER_URL + "/questionspacks/")
            .done(function (packsData) {
              $.each(packsData, function(el) {
                var topics = new app.TopicsCollection();
                $.each(el.topics, function (topicData) {
                  topics.add({name: topicData.models, id: topicData.id});
                });
                app.packs.add({name: el.name, id: el.id, topics: topics});
                console.log(a=app.packs);
              });
            })
            .fail(function (data) {
              alert(data.error);
            });
        })
        .fail(function (data) {
          alert(data.error);
        });
      return this;
    }
  });
});
