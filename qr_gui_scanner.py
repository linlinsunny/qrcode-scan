import tkinter as tk
from tkinter import messagebox
import mss
import pyperclip
from PIL import Image
from pyzbar import pyzbar
import cv2
import numpy as np
import os
import webbrowser
import re

def is_url(text):
    # 简单的URL正则表达式，可以根据需要进行调整
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_pattern, text) is not None

def scan_qr_code_from_screen_gui(status_label):
    status_label.config(text="正在扫描二维码...")
    status_label.update_idletasks() # 立即更新UI

    debug_screenshot_path = "debug_screenshot.png" # 定义调试截图路径

    try:
        with mss.mss() as sct:
            # Grab the data from the main monitor
            sct_img = sct.grab(sct.monitors[1])

            # Create an Image from the raw BGRA data
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

            # Decode the QR codes
            decoded_objects = pyzbar.decode(img)

            if decoded_objects:
                data = decoded_objects[0].data.decode("utf-8")
                pyperclip.copy(data)
                status_label.config(text=f"二维码已找到并复制到剪贴板: {data}")
                messagebox.showinfo("成功", f"二维码已找到并复制到剪贴板: {data}")

                if is_url(data):
                    webbrowser.open(data)
                    status_label.config(text=f"""二维码已找到并复制到剪贴板: {data}
已在浏览器中打开URL。""")
                    messagebox.showinfo("打开URL", f"已在默认浏览器中打开URL: {data}")

            else:
                status_label.config(text="未在屏幕上找到二维码。")
                messagebox.showinfo("未找到", "未在屏幕上找到二维码。")
                # For debugging, save the captured image
                debug_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
                cv2.imwrite(debug_screenshot_path, debug_img)

    except Exception as e:
        status_label.config(text=f"发生错误: {e}")
        messagebox.showerror("错误", f"发生错误: {e}")
    finally:
        # 无论是否找到二维码，都尝试删除调试截图文件
        if os.path.exists(debug_screenshot_path):
            os.remove(debug_screenshot_path)
            print(f"已删除调试截图文件: {debug_screenshot_path}")

def create_gui():
    root = tk.Tk()
    root.title("二维码扫描器")
    root.geometry("400x200") # 设置窗口大小

    # 状态标签
    status_label = tk.Label(root, text="点击按钮开始扫描", wraplength=350)
    status_label.pack(pady=20)

    # 扫描按钮
    scan_button = tk.Button(root, text="识别二维码", command=lambda: scan_qr_code_from_screen_gui(status_label))
    scan_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
