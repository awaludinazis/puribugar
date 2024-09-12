import frappe
import time
from frappe import _
from datetime import datetime
import pytz

@frappe.whitelist(allow_guest=True)
def ping():
    return {
        "msg": "pong",
        }

@frappe.whitelist(allow_guest=True)
def rs1():
    try:
        gate_name = "rs1"
        gate = frappe.get_doc("Gate Tripod", {"gate_name": gate_name})
        if gate:
            frappe.response['msg'] = "success"
            frappe.response['id'] = gate.gate_name
            frappe.response['status_in'] = gate.status_in
            frappe.response['status_out'] = gate.status_out
        else:
            frappe.response['status'] = "error"
            frappe.response['message'] = _("No gate found with the given gate_name.")
        
        return None

    except Exception as e:
        frappe.response['status'] = "error"
        frappe.response['message'] = str(e)
        return None


@frappe.whitelist(allow_guest=True)
def rs2():
    try:
        gate_name = "rs2"
        gate = frappe.get_doc("Gate Tripod", {"gate_name": gate_name})
        if gate:
            frappe.response['msg'] = "success"
            frappe.response['id'] = gate.gate_name
            frappe.response['status_in'] = gate.status_in
            frappe.response['status_out'] = gate.status_out
        else:
            frappe.response['status'] = "error"
            frappe.response['message'] = _("No gate found with the given gate_name.")
        
        return None

    except Exception as e:
        frappe.response['status'] = "error"
        frappe.response['message'] = str(e)
        return None
    
@frappe.whitelist(allow_guest=True)
def verify():
    try:
        gate_name = "rs1"
        data = frappe.local.form_dict
        biometric_id = data.get("info", {}).get("Address")

        if not biometric_id:
            return {
                "status": "error",
                "message": _("Biometric ID is required")
            }
        
        member = frappe.get_doc("Member", {"biometric_id": biometric_id})

        if not member: 
            return {
                "status": "error",
                "message": _("Member not Found")
            }

        # get current time jakarta
        jakarta_timezone = pytz.timezone('Asia/Jakarta')
        current_time = datetime.now(jakarta_timezone)
        current_time_formated = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        attendance_status = "checkin"
        
        member.db_set('last_check_in', current_time_formated)
        member.db_set('attendance_status', attendance_status)
        member.save()

        #update table gate
        status_in = "open"
        gate_tripod = frappe.get_doc("Gate Tripod", {"gate_name": gate_name})
        gate_tripod.db_set('status_in', status_in)
        gate_tripod.save()

        member_gate_history = frappe.get_doc({
            "doctype": "Member Gate History",
            "member_id": member.name,
            "biometric_id": member.biometric_id,
            "check_in": current_time_formated,
            "attendance_status": attendance_status
        })
        member_gate_history.insert()

        frappe.db.commit()

        # sleep 1 detik
        time.sleep(1)
        status_in = "close"
        gate_tripod = frappe.get_doc("Gate Tripod", {"gate_name": gate_name})
        gate_tripod.db_set('status_in', status_in)
        gate_tripod.save()

        frappe.db.commit()

        return {
            "status": "success",
            "message": _("Success open gate")
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error in verify"))
        return {
            "status": "error",
            "message": str(e)
        }

@frappe.whitelist(allow_guest=True)
def heartbeat():
    try:
        operator = "HeartBeat"
        data = frappe.local.form_dict
        operator_fr = data.get("operator")
        device_id = data.get("info", {}).get("DeviceID")
        time_fr = data.get("info", {}).get("Time")

        if operator != operator_fr and device_id is None and time_fr is None:
            return {
                "status": "error",
                "message": _("HeartBeat is stop")
            }
        else:
            return {
                "status": "success",
                "message": _("HeartBeat is working")
            }
        
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error in verify"))
        return {
            "status": "error",
            "message": str(e)
        }    
