
// frappe.ui.form.on('Vcm TicketSP', {

//     refresh: function(frm) {
//         frm.trigger('sp_category');
//     },
//     sp_category: function(frm) {
//         let sub_category_options = '';
//         if (frm.doc.sp_category === 'Farvision') {
//             sub_category_options = [
//                 'Farvision - Backdated Permission',
//                 'Farvision - CRM/PMS Issues',
//                 'Farvision - Document Format',
//                 'Farvision - Document Type Change',
//                 'Farvision - Engineering Module',
//                 'Farvision - Farvision Bug',
//                 'Farvision - Finance Issues',
//                 'Farvision - Item/ Vendor Creation/ Deletion',
//                 'Farvision - Login Issues',
//                 'Farvision - Report',
//                 'Farvision - Rights',
//                 'Farvision - Transaction Delete',
//                 'Farvision - Transaction Error',
//                 'Farvision - Workflow Changes',
//                 'Farvision - Reported by Phone/ Email',
//                 'Farvision - Others'
//             ].join('\n');
//         }  else if (frm.doc.sp_category === 'ERPNext') {
//             sub_category_options = 'ERPNext - POS\nERPNext - TT';
//         } 

//         frm.set_df_property('sp_sub_category', 'options', sub_category_options);

//         // Reset the sub_category value if it doesn't match the new options
//         if (!sub_category_options.split('\n').includes(frm.doc.sp_sub_category)) {
//             frm.set_value('sp_sub_category', '');
//         }
//     },

//     onload: function(frm) {
//         // Check if Email ID, Mobile, or Full Name fields are empty
//         if (!frm.doc.email_id || !frm.doc.mobile || !frm.doc.name1) {
//             // Fetch the creator's email, mobile number, and full name
//             frappe.call({
//                 method: 'frappe.client.get_value',
//                 args: {
//                     doctype: 'User',
//                     filters: { name: frm.doc.owner },
//                     fieldname: ['email', 'mobile_no', 'full_name']
//                 },
//                 callback: function(response) {
//                     if (response.message) {
//                         // Set the email ID if it's empty
//                         if (!frm.doc.email_id && response.message.email) {
//                             frm.set_value('email_id', response.message.email);
//                         }
//                         // Set the mobile number if it's empty
//                         if (!frm.doc.mobile && response.message.mobile_no) {
//                             frm.set_value('mobile', response.message.mobile_no);
//                         }
//                         // Set the full name (mapped to `name1`) if it's empty
//                         if (!frm.doc.name1 && response.message.full_name) {
//                             frm.set_value('name1', response.message.full_name);
//                         }
//                     }
//                     // Make all three fields read-only
//                     frm.set_df_property('email_id', 'read_only', 1);
//                     frm.set_df_property('mobile', 'read_only', 1);
//                     frm.set_df_property('name1', 'read_only', 1);
//                 }
//             });
//         } else {
//             // If the fields are not empty, set them as read-only
//             frm.set_df_property('email_id', 'read_only', 1);
//             frm.set_df_property('mobile', 'read_only', 1);
//             frm.set_df_property('name1', 'read_only', 1);
//         }
//     },
    
    
// });



// frappe.ui.form.on('Vcm TicketSP', {
//     refresh: function(frm) {
//         frm.trigger('sp_category');
//         frm.trigger('update_ticket_aging');
//     },
    
//     sp_category: function(frm) {
//         let sub_category_options = '';
//         if (frm.doc.sp_category === 'Farvision') {
//             sub_category_options = [
//                 'Farvision - Backdated Permission',
//                 'Farvision - CRM/PMS Issues',
//                 'Farvision - Document Format',
//                 'Farvision - Document Type Change',
//                 'Farvision - Engineering Module',
//                 'Farvision - Farvision Bug',
//                 'Farvision - Finance Issues',
//                 'Farvision - Item/ Vendor Creation/ Deletion',
//                 'Farvision - Login Issues',
//                 'Farvision - Report',
//                 'Farvision - Rights',
//                 'Farvision - Transaction Delete',
//                 'Farvision - Transaction Error',
//                 'Farvision - Workflow Changes',
//                 'Farvision - Reported by Phone/ Email',
//                 'Farvision - Others'
//             ].join('\n');
//         } else if (frm.doc.sp_category === 'ERPNext') {
//             sub_category_options = 'ERPNext - POS\nERPNext - TT\nERPNext - New Feature\n ERPNext - Error Screen\nERPNext - User Creation\nERPNext - User Permission/User Rights\nERPNext - Document Cancel/Delete\nERPNext - Report Access\nERPNext - Pos Issues\nERPNext - Budget Issues\nERPNext - Approval Changes\nERPNext - Login Issues';
//         }

//         frm.set_df_property('sp_sub_category', 'options', sub_category_options);

//         // Reset the sub_category value if it doesn't match the new options
//         if (!sub_category_options.split('\n').includes(frm.doc.sp_sub_category)) {
//             frm.set_value('sp_sub_category', '');
//         }
//     },

//     onload: function(frm) {
//         if (!frm.doc.email_id || !frm.doc.mobile || !frm.doc.name1) {
//             frappe.call({
//                 method: 'frappe.client.get_value',
//                 args: {
//                     doctype: 'User',
//                     filters: { name: frm.doc.owner },
//                     fieldname: ['email', 'mobile_no', 'full_name']
//                 },
//                 callback: function(response) {
//                     if (response.message) {
//                         if (!frm.doc.email_id && response.message.email) {
//                             frm.set_value('email_id', response.message.email);
//                         }
//                         if (!frm.doc.name1 && response.message.full_name) {
//                             frm.set_value('name1', response.message.full_name);
//                         }
//                         if (response.message.mobile_no) {
//                             // Auto-fill mobile if available
//                             frm.set_value('mobile', response.message.mobile_no);
//                             frm.set_df_property('mobile', 'read_only', 1);
//                         } else {
//                             // Allow manual entry if mobile_no is missing
//                             frm.set_df_property('mobile', 'read_only', 0);
//                         }
//                     }
//                     // Set other fields to read-only
//                     frm.set_df_property('email_id', 'read_only', 1);
//                     frm.set_df_property('name1', 'read_only', 1);
//                 }
//             });
//         } else {
//             frm.set_df_property('email_id', 'read_only', 1);
//             frm.set_df_property('name1', 'read_only', 1);
//             // Allow manual entry for mobile if it was not auto-filled
//             if (!frm.doc.mobile) {
//                 frm.set_df_property('mobile', 'read_only', 0);
//             } else {
//                 frm.set_df_property('mobile', 'read_only', 1);
//             }
//         }
//     }


    
// });




frappe.ui.form.on('Vcm TicketSP', {
    refresh: function(frm) {
        frm.trigger('sp_category');
        frm.trigger('update_ticket_aging');

        // Show "Re-Open" button only if user has role and status is "Close"
        if (frm.doc.status === 'Close' && frappe.user_roles.includes('Vcm Ticketing User')) {
            frm.add_custom_button('Re-Open', function() {
                frappe.confirm(
                    'Are you sure you want to re-open this ticket?',
                    function() {
                        frappe.call({
                            method: 'vcm_ticketing.api.reopen_ticket',
                            args: {
                                ticket_name: frm.doc.name
                            },
                            callback: function(response) {
                                if (!response.exc) {
                                    frappe.msgprint(response.message);  // Show success message
                                    frm.reload_doc();  // Reload form to update status
                                }
                            }
                        });
                    }
                );
            }).addClass('btn-primary'); // Optional: Highlight button
        }
    },

    sp_category: function(frm) {
        let sub_category_options = '';
        if (frm.doc.sp_category === 'Farvision') {
            sub_category_options = [
                'Farvision - Backdated Permission',
                'Farvision - CRM/PMS Issues',
                'Farvision - Document Format',
                'Farvision - Document Type Change',
                'Farvision - Engineering Module',
                'Farvision - Farvision Bug',
                'Farvision - Finance Issues',
                'Farvision - Item/ Vendor Creation/ Deletion',
                'Farvision - Login Issues',
                'Farvision - Report',
                'Farvision - Rights',
                'Farvision - Transaction Delete',
                'Farvision - Transaction Error',
                'Farvision - Workflow Changes',
                'Farvision - Reported by Phone/ Email',
                'Farvision - Others'
            ].join('\n');
        } else if (frm.doc.sp_category === 'ERPNext') {
            sub_category_options = 'ERPNext - POS\nERPNext - TT\nERPNext - New Feature\nERPNext - Error Screen\nERPNext - User Creation\nERPNext - User Permission/User Rights\nERPNext - Document Cancel/Delete\nERPNext - Report Access\nERPNext - Pos Issues\nERPNext - Budget Issues\nERPNext - Approval Changes\nERPNext - Login Issues';
        }

        frm.set_df_property('sp_sub_category', 'options', sub_category_options);

        // Reset the sub_category value if it doesn't match the new options
        if (!sub_category_options.split('\n').includes(frm.doc.sp_sub_category)) {
            frm.set_value('sp_sub_category', '');
        }
    },

    onload: function(frm) {
        if (!frm.doc.email_id || !frm.doc.mobile || !frm.doc.name1) {
            frappe.call({
                method: 'frappe.client.get_value',
                args: {
                    doctype: 'User',
                    filters: { name: frm.doc.owner },
                    fieldname: ['email', 'mobile_no', 'full_name']
                },
                callback: function(response) {
                    if (response.message) {
                        if (!frm.doc.email_id && response.message.email) {
                            frm.set_value('email_id', response.message.email);
                        }
                        if (!frm.doc.name1 && response.message.full_name) {
                            frm.set_value('name1', response.message.full_name);
                        }
                        if (response.message.mobile_no) {
                            // Auto-fill mobile if available
                            frm.set_value('mobile', response.message.mobile_no);
                            frm.set_df_property('mobile', 'read_only', 1);
                        } else {
                            // Allow manual entry if mobile_no is missing
                            frm.set_df_property('mobile', 'read_only', 0);
                        }
                    }
                    // Set other fields to read-only
                    frm.set_df_property('email_id', 'read_only', 1);
                    frm.set_df_property('name1', 'read_only', 1);
                }
            });
        } else {
            frm.set_df_property('email_id', 'read_only', 1);
            frm.set_df_property('name1', 'read_only', 1);
            // Allow manual entry for mobile if it was not auto-filled
            if (!frm.doc.mobile) {
                frm.set_df_property('mobile', 'read_only', 0);
            } else {
                frm.set_df_property('mobile', 'read_only', 1);
            }
        }
    }
});
