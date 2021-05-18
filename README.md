# SMS Sender

SMS Sender coded in Python for [TextBelt]('https://textbelt.com')

## Features
- Can be used to Send Bulk SMS
- Accepts `numbers.txt` file containing all numbers.
- Shows Message Delivery Status, Current Sending Number for Each Messages
- Shows Total Sent, Successed, Failed Messages Count, Remaining SMS Quota
- Accurately Detects Failed Messages
- Logs Failed Numbers in `error_log.txt`
- Checks Internet Connection Availability aborts if Disconnected
- Faster Delivery

### Installation
- clone this repository<br>
`git clone https://github.com/akshayitzme/sms-sender`
- Set your api key in [config.py]('/config.py')
### Usage
  `python sms-sender.py`
### API
[TextBelt]('https://textbelt.com')