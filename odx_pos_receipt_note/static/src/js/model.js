odoo.define("odx_pos_receipt_note.models", function (require) {
"use strict";

    var models = require('point_of_sale.models');

    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
         export_for_printing: function () {
            var res = _super_orderline.export_for_printing.apply(this, arguments);
            res.note = this.note;
            return res;
     },
    });
});