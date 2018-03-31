REQUEST_SMS_XML_FORMAT = """
<request>
<sms-id>{api_id}</sms-id>
<access-token>{access_token}</access-token>
<response-format>xml</response-format>
<method>{method_name}</method>
<params>
<send_type>{sms_type}</send_type>
<ref_key>{key}</ref_key>
<subject>{title}</subject>
<message>{message}</message>
<callback>{sender}</callback>
<phone>{receiver}</phone>
<reserve>{scheduled_time}</reserve>
</params>
</request>
"""

REQUEST_SMS_RESULT_FORMAT = """
<request>
<sms-id>{api_id}</sms-id>
<access-token>{access_token}</access-token>
<response-format>xml</response-format>
<method>SMS.getStatusByRef</method>
<params>
<ref_key>{key}</ref_key>
</params>
</request>
"""

REQUEST_RESERVE_CANCEL_FORMAT = """
<request>
<sms-id>{api_id}</sms-id>
<access-token>{access_token}</access-token>
<response-format>xml</response-format>
<method>SMS.reservationCancel</method>
<params>
<ref_key>{key}</ref_key>
<send_type>{sms_type}</send_type>
<phonenum>{receiver}</phonenum>
</params>
</request>
"""
