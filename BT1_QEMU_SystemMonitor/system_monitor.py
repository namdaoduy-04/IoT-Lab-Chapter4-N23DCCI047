import psutil
from datetime import datetime
from time import sleep

# Bước 5 & 6: Mở file log và chuẩn bị đóng file sạch
log_file = open('system_log.txt', 'w')

print("--- He thong bat dau theo doi ---")
print("Nhan Ctrl+C de dung va luu log.")

try:
    while True:
        # Bước 2: Đọc CPU usage
        cpu_list = psutil.cpu_percent(interval=1, percpu=True)
        cpu_avg = sum(cpu_list) / len(cpu_list)

        # Bước 7: Logic phân loại trạng thái (Sử dụng 4 dấu cách cho mỗi cấp thụt lề)
        if cpu_avg >= 70:
            status = 'CRITICAL'
        elif cpu_avg >= 30:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        # Bước 3: Đọc RAM và Disk
        ram = psutil.virtual_memory()
        ram_used_mb = ram.used // (1024 ** 2)
        ram_total_mb = ram.total // (1024 ** 2)
        ram_pct = ram.percent

        disk = psutil.disk_usage('/')
        disk_pct = disk.percent

        # Bước 4: Tạo format output đúng yêu cầu
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = (f'[{now}] CPU: {cpu_avg:.1f}% | RAM: {ram_used_mb}/{ram_total_mb} MB '
        f'({ram_pct}%) | Disk: {disk_pct}% | {status}')


        # In ra Terminal
        print(line)

        # Bước 7: In cảnh báo riêng nếu không phải NORMAL
        if status != 'NORMAL':
            print(f'  ⚠ {status}: CPU dang o muc cao {cpu_avg:.1f}%')

        # Bước 5: Ghi vào file log và flush dữ liệu
        log_file.write(line + '\n')
        log_file.flush()

        # Bước 4: Lặp mỗi 2 giây
        sleep(2)

except KeyboardInterrupt:
    # Bước 6: Bắt Ctrl+C
    print('\n[Thong bao] Da bam Ctrl+C. Dang dung chuong trinh...')

finally:
    # Bước 6: Đóng file an toàn
    log_file.close()
    print('Log da duoc luu vao system_log.txt. Tam biet!')
