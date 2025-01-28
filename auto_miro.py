from pywinauto.application import Application
import pyautogui
import time

# Setup variables
loop_delay = 0.5
tcode = "MIRO"

data = {
    'documentDate': '31122024',
    'reference': '000081',
    'postingDate': '15012025',
    'amount': 2530000,
    'text': 'KUE SOFI',
    'po': '4516000001',
    'nomorFaktur': '000.000-00.00000000',
    'tanggalFaktur': '31122024',
    'nomorVerifikasi': '92570',
    'nik': 'R.9293',
    'top': 45,
    'purchaser': 'G03- Dept HRD & GA'
}

# Start SAP GUI
app = Application(backend='uia').connect(title_re="SAP Easy Access")

# Accessing SAP Easy Access window
sap_easy_access_window = app.window(title_re="SAP Easy Access")

# Locate the TCode form and enter a TCode
tcode_combobox = sap_easy_access_window.child_window(auto_id="200", control_type="ComboBox")
tcode_edit = tcode_combobox.child_window(auto_id="1001", control_type="Edit")
tcode_edit.type_keys(tcode, with_spaces=True)
tcode_edit.type_keys("{ENTER}")

time.sleep(1)

# Document Date field
pyautogui.typewrite(data.get("documentDate"))
for i in range(2):
    pyautogui.press('enter')
    time.sleep(loop_delay)

# Reference field
pyautogui.hotkey('tab')
pyautogui.typewrite(data.get("reference"))
time.sleep(0.5)

# Posting date field
pyautogui.hotkey('tab')
pyautogui.typewrite(data.get("postingDate"))
time.sleep(0.5)

# Amount field
pyautogui.hotkey('tab')
pyautogui.typewrite(str(data.get("amount")))
time.sleep(0.5)

# Calculate Tax checkbox
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.press('space')
time.sleep(0.5)

# Text field
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite(data.get("text"))

# Move to PO field
for i in range(2):
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(loop_delay)

pyautogui.press('tab')

# PO field
pyautogui.typewrite(data.get("po"))
pyautogui.press('enter')
time.sleep(0.5)

# Move to Faktur No field
for i in range(8):  # 8 for Production Server and 1 for Development Server
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(loop_delay)

for i in range(5):
    pyautogui.press('tab')
    time.sleep(loop_delay)

# Faktur No field
pyautogui.typewrite(data.get("nomorFaktur"))
time.sleep(0.5)

# Tgl Faktur field
pyautogui.press('tab')
pyautogui.typewrite(data.get("tanggalFaktur"))
time.sleep(0.5)

# Invoice Verif checkbox
pyautogui.press('tab')
pyautogui.press('space')
time.sleep(0.5)

# Verif No field
pyautogui.press('tab')
pyautogui.typewrite(data.get("nomorVerifikasi"))
time.sleep(0.5)

# NIK field
pyautogui.press('tab')
pyautogui.typewrite(data.get("nik"))
time.sleep(0.5)

# Move tab to Payment tab
for i in range(9):
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(loop_delay)

pyautogui.press('right')
time.sleep(0.5)

for i in range(1):  # 2 for Production Server and 1 for Development Server
    pyautogui.press('enter')
    time.sleep(0.5)

# Move to Payt Terms field
for i in range(7):
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(loop_delay)

for i in range(2):
    pyautogui.press('tab')
    time.sleep(loop_delay)

# Payt Terms field
pyautogui.typewrite(str(data.get("top")))

# Move to Details tab
for i in range(10):
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(loop_delay)

pyautogui.press('right')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(0.5)

# # Move to Assignment field
# for i in range(7):
#     pyautogui.hotkey('ctrl', 'tab')
#     time.sleep(loop_delay)

# for i in range(4):
#     pyautogui.press('tab')
#     time.sleep(loop_delay)

# # Assigmnment field
# pyautogui.typewrite('G03- Dept HRD & GA')

# # Header Text field
# pyautogui.press('tab')
# pyautogui.typewrite('KUE SOFI')

# If success
print("Success!!")