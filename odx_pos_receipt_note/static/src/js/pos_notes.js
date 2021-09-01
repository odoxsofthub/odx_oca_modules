
odoo.define('odx_pos_receipt_note.notes', function (require) {
"use strict";
    var pos_model = require('point_of_sale.models');
    var core = require('web.core');
    var _t = core._t;
    var SuperOrder = pos_model.Order;
    const ProductScreen = require('point_of_sale.ProductScreen');
    var SuperOrderline = pos_model.Orderline;
    const PosComponent = require('point_of_sale.PosComponent');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');

    class OrderlineNoteButtonExt extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        get currentOrder(){
            return this.env.pos.get_order();
        }
        get selectedOrderline() {
            return this.env.pos.get_order().get_selected_orderline();
        }
         async onClick() {
            if (!this.selectedOrderline) return;

            const { confirmed, payload: inputNote } = await this.showPopup('TextAreaPopup', {
                startingValue: this.selectedOrderline.get_note(),
                title: this.env._t('Add Note'),
            });

            if (confirmed) {
                this.selectedOrderline.set_note(inputNote);
            }
        }

    }

    OrderlineNoteButtonExt.template = 'OrderlineNoteButton';

    ProductScreen.addControlButton({
        component: OrderlineNoteButtonExt,
        condition: function() {
            console.log("this",this.env.pos.config.iface_orderline_pos_order_notes)
            return this.env.pos.config.iface_orderline_pos_order_notes;
        },
    });

    Registries.Component.add(OrderlineNoteButtonExt);

    return OrderlineNoteButtonExt;

});

