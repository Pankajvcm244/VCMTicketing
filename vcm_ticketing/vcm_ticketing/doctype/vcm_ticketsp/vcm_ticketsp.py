# from frappe.model.document import Document
# import frappe

# class VcmTicketSP(Document):
#     def validate(self):
#         # Send an email on every save
#         self.send_email()

#     def send_email(self):
#         submitter_email = self.email_id  
#         cc_email = "lokesh.sisodiya@vcm.org.in,amansoniofficial20@gmail.com"  

#         if not submitter_email:
#             frappe.log_error("Submitter email is missing for ticket: " + self.name, "Email Sending Error")
#             return
            
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
#                 <td>{self.sp_category}</td>
#             </tr>
#             <tr>
#                 <td><b>Status</b></td>
#                 <td>{self.sp_sub_category}</td>
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
#                 <td><b>Area of Service</b></td>
#                 <td>{self.priority}</td>
#             </tr>
#             <tr>
#                 <td><b>Description</b></td>
#                 <td>{self.description}</td>
#             </tr>
#         </table>
#         <br>
#         <p>Thank you.<br>Best regards,<br>Your Support Team</p>
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

# class VcmTicketSP(Document):
#     def before_save(self):
#         """Send an email only when the ticket status changes to avoid duplicate emails."""
#         if self.has_value_changed("status"):  # Only send email when the status changes
#             self.send_email()

#     def send_email(self):
#         submitter_email = self.email_id  # Ensure this field exists in your Doctype
#         cc_email = "lokesh.sisodiya@vcm.org.in,amansoniofficial20@gmail.com"  

#         if not submitter_email:
#             frappe.log_error(f"Submitter email is missing for ticket: {self.name}", "Email Sending Error")
#             return
            
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
#                 <td><b>Category</b></td>
#                 <td>{self.sp_category}</td>
#             </tr>
#             <tr>
#                 <td><b>Sub Category</b></td>
#                 <td>{self.sp_sub_category}</td>
#             </tr>
#             <tr>
#                 <td><b>Current Status</b></td>
#                 <td>{self.status}</td>
#             </tr>
#             <tr>
#                 <td><b>Assigned To</b></td>
#                 <td>{self.assigned_to}</td>
#             </tr>
#             <tr>
#                 <td><b>Priority</b></td>
#                 <td>{self.priority}</td>
#             </tr>
#             <tr>
#                 <td><b>Description</b></td>
#                 <td>{self.description}</td>
#             </tr>
#         </table>
#         <br>
#         <p>Thank you.<br>Best regards,<br>Your Support Team</p>
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

class VcmTicketSP(Document):
    def before_save(self):
        """Send an email only when the ticket status changes to avoid duplicate emails."""
        if self.has_value_changed("status"):  # Only send email when the status changes
            self.send_email()

    def send_email(self):
        submitter_email = self.email_id  # Ensure this field exists in your Doctype
        cc_email = "lokesh.sisodiya@vcm.org.in,amansoniofficial20@gmail.com"  

        if not submitter_email:
            frappe.log_error(f"Submitter email is missing for ticket: {self.name}", "Email Sending Error")
            return
            
        subject = f"🔔 Ticket Update: {self.name} - {self.status}"
        
        message = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: auto; border: 1px solid #ddd; border-radius: 8px; overflow: hidden; background-color: #f9f9f9;">
            <div style="background-color: #0073e6; padding: 15px; text-align: center; color: #ffffff; font-size: 20px;">
                🎫 Ticket Update Notification
            </div>
            <div style="padding: 20px; color: #333;">
                <p style="font-size: 16px;">Dear <b>{self.name1}</b>,</p>
                <p style="font-size: 14px; line-height: 1.5;">
                    Your ticket <b>{self.name}</b> has been updated. Please find the details below:
                </p>
                <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
                    <tr style="background-color: #0073e6; color: #ffffff;">
                        <th style="padding: 10px; text-align: left;">Field</th>
                        <th style="padding: 10px; text-align: left;">Details</th>
                    </tr>
                    <tr style="background-color: #f2f7fd;">
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Category</b></td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{self.sp_category}</td>
                    </tr>
                    <tr style="background-color: #ffffff;">
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Sub Category</b></td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{self.sp_sub_category}</td>
                    </tr>
                    <tr style="background-color: #f2f7fd;">
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Current Status</b></td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd; color: #d9534f;"><b>{self.status}</b></td>
                    </tr>
                    <tr style="background-color: #ffffff;">
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Assigned To</b></td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{self.assigned_to}</td>
                    </tr>
                    <tr style="background-color: #f2f7fd;">
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Priority</b></td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{self.priority}</td>
                    </tr>
                    <tr style="background-color: #ffffff;">
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Description</b></td>
                        <td style="padding: 8px; border-bottom: 1px solid #ddd;">{self.description}</td>
                    </tr>
                </table>
                <p style="font-size: 14px; margin-top: 15px;">
                    For further assistance, please contact our support team.
                <p style="text-align: center; margin-top: 20px;">
                    <a href="{frappe.utils.get_url()}/app/vcm-ticket-it/{self.name}" 
                        style="background-color: #0073e6; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">
                        View Ticket
                    </a>
                </p>
                <p style="font-size: 12px; color: #777; text-align: center; margin-top: 20px;">
                    Thank you! <br> <b>Your Support Team</b>
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
