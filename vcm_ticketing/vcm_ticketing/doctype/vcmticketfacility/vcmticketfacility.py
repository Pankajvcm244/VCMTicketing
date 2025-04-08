

from frappe.model.document import Document
import frappe

class VcmTicketFacility(Document):
    def validate(self):
        # Send an email on every save
        self.send_email()

    def send_email(self):
        submitter_email = self.email_id  
        cc_email = "vswd@vcm.org.in,saurabh.tyagi@vcm.org.in,Facility.vrn@vcm.org.in" 

        if not submitter_email:
            frappe.log_error("Submitter email is missing for ticket: " + self.name, "Email Sending Error")
            return
            
        subject = f"🔔 Ticket Update: {self.name} - {self.status}"

        # Modern HTML Email Template
        message = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f4;">
            <div style="max-width: 600px; background: #ffffff; padding: 20px; border-radius: 8px; 
                        box-shadow: 0px 0px 10px rgba(0,0,0,0.1);">
                <h2 style="color: #0073e6; text-align: center;">🎫 Facility Support Ticket Update</h2>
                <p>Dear <b>{self.name1}</b>,</p>
                <p>Your ticket <b>#{self.name}</b> status has been updated to 
                   <b style="color: #28a745;">{self.status}</b>.</p>
                
                <table style="width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 14px;">
                    <tr style="background-color: #0073e6; color: white;">
                        <th style="padding: 10px; text-align: left;">Field</th>
                        <th style="padding: 10px; text-align: left;">Details</th>
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
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Department</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.department}</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Area of Service</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.area_of_service}</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Description</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.description}</td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><b>Comment/Solution</b></td>
                        <td style="border: 1px solid #ddd; padding: 8px;">{self.comment}</td>
                    </tr>
                </table>

               
                <p style="font-size: 12px; color: #777; text-align: center;">
                    If you have any questions, please contact our support team.
                </p>

                <p style="text-align: center; color: #333; font-size: 14px;">
                    Thank you,<br><b>Your Support Team</b>
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

