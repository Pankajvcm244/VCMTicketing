// Copyright (c) 2025, Pankaj Sharma and contributors
// For license information, please see license.txt

// frappe.ui.form.on("VcmTicketFacility", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('VcmTicketFacility', {
     onload: function(frm) {
        // Check if Email ID, Mobile, or Full Name fields are empty
        if (!frm.doc.email_id || !frm.doc.mobile || !frm.doc.full_name) {
            // Fetch the creator's email, mobile number, and full name
            frappe.call({
                method: 'frappe.client.get_value',
                args: {
                    doctype: 'User',
                    filters: { name: frm.doc.owner },
                    fieldname: ['email', 'full_name']
                },
                callback: function(response) {
                    if (response.message) {
                        // Set the email ID if it's empty
                        if (!frm.doc.email_id && response.message.email) {
                            frm.set_value('email_id', response.message.email);
                        }
                        // Set the mobile number if it's empty
                        
                        // Set the full name if it's empty
                        if (!frm.doc.full_name && response.message.full_name) {
                            frm.set_value('name1', response.message.full_name);
                        }
                    }
                    // Make all three fields read-only
                    frm.set_df_property('email_id', 'read_only', 1);
                   
                    frm.set_df_property('name1', 'read_only', 1);
                }
            });
        } else {
            // If the fields are not empty, set them as read-only
            frm.set_df_property('email_id', 'read_only', 1);
            
            frm.set_df_property('name1', 'read_only', 1);
        }
    }

});
