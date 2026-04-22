from machine import Pin, ADC
import time

# Khai báo ADC tại chân GP26
pot = ADC(Pin(26))

# Khai báo các chân LED
red = Pin(15, Pin.OUT)
yellow = Pin(14, Pin.OUT)
green = Pin(13, Pin.OUT)

while True:
    raw = pot.read_u16()              # Đọc giá trị từ 0 – 65535
    percent = raw / 65535 * 100       # Chuyển sang phần trăm

    if percent < 33:
        # Mức thấp: Chỉ LED xanh sáng
        green.value(1); yellow.value(0); red.value(0)
        level = 'THẤP'
    elif percent < 66:
        # Mức trung bình: Xanh và Vàng sáng
        green.value(1); yellow.value(1); red.value(0)
        level = 'TRUNG BÌNH'
    else:
        # Mức cao: Cả 3 LED cùng sáng
        green.value(1); yellow.value(1); red.value(1)
        level = 'CAO'

    # In kết quả ra màn hình Terminal
    print(f'ADC: {raw:5d} | {percent:5.1f}% | {level}')
    time.sleep(0.5)
