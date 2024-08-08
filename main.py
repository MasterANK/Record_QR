#pip install qrcode
import qrcode
import pandas as pd
import os

excel_file = "/content/TestData.xlsx"  # CHANGE THIS
df = pd.read_excel(excel_file)

qr_path = "QR_Folder"
os.mkdir(qr_path)

for index, row in df.iterrows():
    data = ', '.join(map(str, row.values))

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(f"{qr_path}/qrcode_row_{index}.png")

    print(f"Data {index} Saved") ## Testing

print("QR codes generated and saved successfully.")
