import matplotlib
matplotlib.use('Agg')  # Bắt buộc cho QEMU headless
import matplotlib.pyplot as plt
from sensor_sim import SimUltrasonic, SimPotentiometer
from time import sleep

# Khởi tạo cảm biến
us = SimUltrasonic(echo=24, trigger=23, base_distance=50.0)
pot = SimPotentiometer(initial_value=0.4)  # span = 40cm
span = pot.value * 100  # Chuyển sang cm

# Thu thập 50 mẫu
distances = []
for i in range(50):
    d = us.distance
    distances.append(d)
    print(f"  Mẫu {i+1}/50: {d:.1f} cm")
    sleep(0.1)  # Rút ngắn cho nhanh (thực tế 0.5s)

print(f"\nThu thập xong {len(distances)} mẫu.")

# Vẽ đồ thị
fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(distances))

# Line plot khoảng cách
ax.plot(x, distances, 'b-', linewidth=1.5, label='Khoảng cách (cm)')

# Đường ngưỡng span (đỏ, nét đứt)
ax.axhline(y=span, color='r', linestyle='--', linewidth=2, label=f'Span = {span:.0f} cm')

# Tô vùng Span (distance < span)
ax.fill_between(x, 0, [min(d, span) for d in distances],
                 alpha=0.2, color='red', label='Vùng Span!')

# Nhãn trục + tiêu đề
ax.set_title('Ultrasonic Sensor Simulation — Span Detection')
ax.set_xlabel('Sample')
ax.set_ylabel('Distance (cm)')
ax.set_ylim(0, max(distances) + 10)
ax.legend(loc='upper right')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sensor_chart.png', dpi=150)
print('Saved: sensor_chart.png')
