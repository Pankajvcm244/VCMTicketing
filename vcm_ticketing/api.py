import frappe

@frappe.whitelist()
def reopen_ticket(ticket_name):
    try:
        frappe.flags.ignore_permissions = True  # Bypass permissions
        frappe.db.set_value("Vcm TicketSP", ticket_name, "status", "Re-Open")
        frappe.db.commit()
        return "Ticket Re-Opened Successfully"
    except Exception as e:
        frappe.log_error(f"Error reopening ticket: {str(e)}", "Vcm TicketSP Error")
        frappe.throw("An error occurred while reopening the ticket. Please contact the administrator.")
