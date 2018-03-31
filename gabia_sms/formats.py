REQUEST_SMS_XML_FORMAT = """
<request>
<sms-id>{api_id}</sms-id>
<access-token>{access_token}</access-token>
<response-format>xml</response-format>
<method>SMS.send</method>
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
