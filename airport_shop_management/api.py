import frappe

def update_shop_counts(doc, method):
    airport_name = doc.airport

    total_shops = frappe.db.count('Shop', filters={'airport': airport_name})
    occupied_shops = frappe.db.count('Shop', filters={'airport': airport_name, 'status': 'Occupied'})
    
    available_shops = total_shops - occupied_shops

    frappe.db.set_value('Airports', airport_name, 'total_shops', total_shops)
    frappe.db.set_value('Airports', airport_name, 'occupied_shops', occupied_shops)
    frappe.db.set_value('Airports', airport_name, 'available_shops', available_shops)

# import frappe
# from frappe.utils import nowdate
# from frappe.core.doctype.communication.email import make

def send_rent_reminders():
    pass
    # # Check if reminders are enabled in the Airport Shop Setting
    # settings = frappe.get_single("Airport Shop Setting")
    # if not settings.enable_rent_reminders:
    #     return

    # # Get all shops with unpaid rent
    # unpaid_rent_shops = frappe.get_all(
    #     "Rent Payment",
    #     filters={"rent_status": "Unpaid"},
    #     fields=["shop", "tenant", "amount"]
    # )
    
    # for rent in unpaid_rent_shops:
    #     tenant = frappe.get_doc("Tenant", rent.tenant)
    #     shop = frappe.get_doc("Shop", rent.shop)
        
    #     # Send email reminder to tenant
    #     message = f"""
    #         Dear {tenant.tenant_name},
    #         This is a reminder that your rent for shop {shop.shop_name} is due. 
    #         Amount: {rent.amount}
    #         Please make the payment by the due date to avoid penalties.
    #     """
        
    #     make(
    #         recipients=[tenant.email],
    #         subject="Rent Due Reminder",
    #         content=message,
    #         send_email=True
    #     )
