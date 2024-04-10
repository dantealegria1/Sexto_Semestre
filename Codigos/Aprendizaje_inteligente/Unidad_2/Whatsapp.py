import pywhatkit

phone_numer = '+52 4493957174'
group_id = ''
message = "te amo"
time_hour = 12
time_minute = 51
waiting_time_to_send = 20
close_tab = False
waiting_time_to_close = 2

mode = "contact"

if mode == "contact":
    # Send a message to the phone number.
    pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
elif mode == "group":
    pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
else:
    print("Error code: 97654")
    print("Error Message: Please select a mode to send your message.")