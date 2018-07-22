odoo.define('facebook.facebook_page', function (require) {
"use strict";
    var Class = require('web.Class');
    var Widget = require('web.Widget');
    var core = require('web.core');
    var utils = require('web.utils');
    var _t = core._t;
    var _lt = core._lt;

    var homePage = Widget.extend({
        template: 'Page',
        init: function(parent) {
            this._super(parent);
            console.log("init");
        },
        start: function() {
            console.log("start");
        },
    });
    core.action_registry.add('page', homePage);

});