frappe.ui.form.on('Vcm TicketIT', {
    refresh: function (frm) {
        frm.trigger('it_category');
    },
    it_category: function (frm) {
        let it_sub_category_options = '';
        if (frm.doc.it_category === 'Desktop Issue') {
            it_sub_category_options = [
                'Software Issue',
                'Hardware Issue',
                'Peripheral Issue (e.g., keyboard, mouse)'
            ].join('\n');
        } else if (frm.doc.it_category === 'Laptop Issue') {
            it_sub_category_options = [
                'Software Issue',
                'Hardware Issue',
                'Battery or Power Issue'
            ].join('\n');
        } else if (frm.doc.it_category === 'Printer Issue') {
            it_sub_category_options = [
                'Printing Quality Issue',
                'Paper Jam or Feeding Issue',
                'Connectivity Issue',
                'Ink Refill or Cartridge Refill'
            ].join('\n');
        } else if (frm.doc.it_category === 'Network Issue') {
            it_sub_category_options = [
                'Connectivity Issue (Wired or Wireless)',
                'Internet Access Issue',
                'Network Speed or Performance Issue'
            ].join('\n');
        } else if (frm.doc.it_category === 'Asset Purchase Request') {
            it_sub_category_options = [
                'New Desktop, Laptop, Printer, etc.',
                'Additional Peripheral (e.g., monitor, keyboard)',
                'Network Equipment (e.g., router, switch)'
            ].join('\n');
        }

        frm.set_df_property('it_sub_category', 'options', it_sub_category_options);

        // Reset the it_sub_category value if it doesn't match the new options
        if (!it_sub_category_options.split('\n').includes(frm.doc.it_sub_category)) {
            frm.set_value('it_sub_category', '');
        }
    },

    onload: function(frm) {
        // Check if Email ID, Mobile, or Full Name fields are empty
        if (!frm.doc.email_id || !frm.doc.contact || !frm.doc.name1) {
            // Fetch the creator's email, mobile number, and full name
            frappe.call({
                method: 'frappe.client.get_value',
                args: {
                    doctype: 'User',
                    filters: { name: frm.doc.owner },
                    fieldname: ['email', 'mobile_no', 'full_name']
                },
                callback: function(response) {
                    if (response.message) {
                        // Set the email ID if it's empty
                        if (!frm.doc.email_id && response.message.email) {
                            frm.set_value('email_id', response.message.email);
                        }
                        // Set the full name if it's empty
                        if (!frm.doc.name1 && response.message.full_name) {
                            frm.set_value('name1', response.message.full_name);
                        }
                        // Set the mobile number if available, otherwise allow manual entry
                        if (response.message.mobile_no) {
                            frm.set_value('contact', response.message.mobile_no);
                            frm.set_df_property('contact', 'read_only', 1); // Make mobile read-only if fetched
                        } else {
                            frm.set_df_property('contact', 'read_only', 0); // Allow manual entry
                        }
                    }
                    // Make Email and Name fields read-only
                    frm.set_df_property('email_id', 'read_only', 1);
                    frm.set_df_property('name1', 'read_only', 1);
                }
            });
        } else {
            // If the fields are already filled, set them as read-only except mobile
            frm.set_df_property('email_id', 'read_only', 1);
            frm.set_df_property('name1', 'read_only', 1);
            
            // Allow manual entry for mobile if it was not fetched
            if (!frm.doc.contact) {
                frm.set_df_property('contact', 'read_only', 0);
            } else {
                frm.set_df_property('contact', 'read_only', 1);
            }
        }
    }

});