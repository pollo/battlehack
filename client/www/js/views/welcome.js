define([
  "app",
  "text!templates/welcome.html",
], function (app, template) {
  app.WelcomeView = Backbone.View.extend({
    el: '#afui',

    render: function () {
      $('.app-loading').hide();
      $(this.el).html(template);

      $.ui.launch();
      return this;
    }
  });
});
