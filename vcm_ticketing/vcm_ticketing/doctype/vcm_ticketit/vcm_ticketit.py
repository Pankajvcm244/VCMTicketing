# import frappe
# from frappe.model.document import Document

# class VcmTicketIT(Document):
#     def validate(self):
#         # Send an email on every save
#         self.send_email()

#     def send_email(self):
#         submitter_email = self.email_id  
#         cc_email = "lokesh.sisodiya@vcm.org.in"  # Update this if needed

#         # Ensure submitter email is present
#         if not submitter_email:
#             frappe.log_error(f"Submitter email is missing for ticket: {self.name}", "Email Sending Error")
#             return

#         # Email subject and body
#         subject = f"Update on your Ticket: {self.name}"
#         message = f"""
#         <p>Dear {self.name1},</p>  <!-- Update {self.name1} with the correct field -->
#         <p>The status of your ticket <b>'{self.name}'</b> has been updated to <b>'{self.status}'</b>.</p>
#         <br>
#         <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
#             <tr>
#                 <th style="background-color: #f2f2f2;">Field</th>
#                 <th style="background-color: #f2f2f2;">Details</th>
#             </tr>
#             <tr>
#                 <td><b>Status</b></td>
#                 <td>{self.status}</td>
#             </tr>
#             <tr>
#                 <td><b>Assigned To</b></td>
#                 <td>{self.assigned_to}</td>
#             </tr>
#             <tr>
#                 <td><b>Category</b></td>
#                 <td>{self.it_category}</td>
#             </tr>
#             <tr>
#                 <td><b>Sub Category</b></td>
#                 <td>{self.it_sub_category}</td>
#             </tr>
#             <tr>
#                 <td><b>Description</b></td>
#                 <td>{self.description}</td>
#             </tr>
#             <tr>
#                 <td><b>Solution</b></td>
#                 <td>{self.solution}</td>
#             </tr>
#         </table>
#         <br>
#         <p>Thank you.<br>Best regards,<br>Your IT Support Team</p>
#         """

#         try:
#             frappe.sendmail(
#                 recipients=[submitter_email],
#                 cc=cc_email.split(","),
#                 subject=subject,
#                 message=message
#             )
#         except Exception as e:
#             frappe.log_error(f"Failed to send email for ticket: {self.name}. Error: {str(e)}", "Email Sending Error")



# import frappe
# from frappe.model.document import Document

# class VcmTicketIT(Document):
#     def before_save(self):
#         """Send an email only when the ticket status is changed."""
#         if self.has_value_changed("status"):  # Check if status field has changed
#             self.send_email()

#     def send_email(self):
#         submitter_email = self.email_id  
#         cc_email = "lokesh.sisodiya@vcm.org.in"  # Update this if needed

#         # Ensure submitter email is present
#         if not submitter_email:
#             frappe.log_error(f"Submitter email is missing for ticket: {self.name}", "Email Sending Error")
#             return

#         # Email subject and body
#         subject = f"Update on your Ticket: {self.name}"
#         message = f"""
#         <p>Dear {self.name1},</p>
#         <p>The status of your ticket <b>'{self.name}'</b> has been updated to <b>'{self.status}'</b>.</p>
#         <br>
#         <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; width: 100%;">
#             <tr>
#                 <th style="background-color: #f2f2f2;">Field</th>
#                 <th style="background-color: #f2f2f2;">Details</th>
#             </tr>
#             <tr>
#                 <td><b>Status</b></td>
#                 <td>{self.status}</td>
#             </tr>
#             <tr>
#                 <td><b>Assigned To</b></td>
#                 <td>{self.assigned_to}</td>
#             </tr>
#             <tr>
#                 <td><b>Category</b></td>
#                 <td>{self.it_category}</td>
#             </tr>
#             <tr>
#                 <td><b>Sub Category</b></td>
#                 <td>{self.it_sub_category}</td>
#             </tr>
#             <tr>
#                 <td><b>Description</b></td>
#                 <td>{self.description}</td>
#             </tr>
#             <tr>
#                 <td><b>Solution</b></td>
#                 <td>{self.solution}</td>
#             </tr>
#         </table>
#         <br>
#         <p>Thank you.<br>Best regards,<br>Your IT Support Team</p>
#         """

#         try:
#             frappe.sendmail(
#                 recipients=[submitter_email],
#                 cc=cc_email.split(","),
#                 subject=subject,
#                 message=message
#             )
#         except Exception as e:
#             frappe.log_error(f"Failed to send email for ticket: {self.name}. Error: {str(e)}", "Email Sending Error")



import frappe
from frappe.model.document import Document

class VcmTicketIT(Document):
    def before_save(self):
        """Send an email only when the ticket status is changed."""
        if self.has_value_changed("status"):  # Check if status field has changed
            self.send_email()

    def send_email(self):
        submitter_email = self.email_id  
        cc_email = "lokesh.sisodiya@vcm.org.in"  # Update this if needed

        # Ensure submitter email is present
        if not submitter_email:
            frappe.log_error(f"Submitter email is missing for ticket: {self.name}", "Email Sending Error")
            return

        # Email subject
        subject = f"🔔 Ticket Update: {self.name} - {self.status}"

        # HTML Email Template
        message = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f4;">
            <div style="max-width: 600px; background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
                <h2 style="color: #0073e6; text-align: center;">IT Support Ticket Update</h2>
                <p>Dear <b>{self.name1}</b>,</p>
                <p>Your IT support ticket <b>#{self.name}</b> has been updated to <b style="color: #28a745;">{self.status}</b>.</p>
                
                <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background-color: #0073e6; color: white;">
                        <th style="padding: 8px; text-align: left;">Field</th>
                        <th style="padding: 8px; text-align: left;">Details</th>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Status</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.status}</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Assigned To</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.assigned_to}</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Category</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.it_category}</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Sub Category</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.it_sub_category}</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Description</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.description}</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Solution</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.solution}</td>
                    </tr>
                </table>

                <p style="text-align: center; margin-top: 20px;">
                    <a href="{frappe.utils.get_url()}/app/vcm-ticket-it/{self.name}" 
                        style="background-color: #0073e6; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                        View Ticket
                    </a>
                </p>

                <p style="font-size: 12px; color: #777; text-align: center;">
                    If you have any questions, please contact our IT support team.
                </p>
            </div>
        </div>
        """

        try:
            frappe.sendmail(
                recipients=[submitter_email],
                cc=cc_email.split(","),
                subject=subject,
                message=message
            )
        except Exception as e:
            frappe.log_error(f"Failed to send email for ticket: {self.name}. Error: {str(e)}", "Email Sending Error")
