# QR GUI Scanner / 二维码桌面识别工具

## 简介 | Introduction

**中文**：
一个基于 Python 的桌面二维码识别工具，支持一键截图并自动识别屏幕上的二维码，复制内容到剪贴板，并自动打开 URL。现在好多发夸克资源的都只留二维码不留链接，在桌面端很难搞，要复制下来然后在找工具。这个脚本先截屏然后分析二维码直接复制到剪贴板，检测到是 url 就直接打开。然后删除截图。

**English**：
A Python-based desktop QR code scanner. It captures your screen, automatically detects QR codes, copies the result to clipboard, and opens URLs in your browser.

---

## 功能简介 | Features

- 截取主显示器屏幕内容，自动识别二维码。
- 识别到二维码后自动复制内容到剪贴板。
- 如果内容为 URL，自动在默认浏览器中打开。
- 简单易用的图形界面。

- Capture the main monitor and auto-detect QR codes.
- Copy the decoded result to clipboard automatically.
- If the result is a URL, open it in your default browser.
- Simple and user-friendly GUI.

---

## 依赖环境 | Requirements

- Python 3.7+
- 推荐在 macOS、Windows、Linux 下使用 (Recommended for macOS, Windows, Linux)

---

## 安装依赖 | Install dependencies

macos 可能需要安装 zbar
brew install zbar

```bash
pip install -r requirements.txt
```

---

## 运行方法 | How to run

```bash
python qr_gui_scanner.py
```

---

## 依赖列表 | Dependency list

- tkinter（标准库，GUI / built-in, GUI）
- mss（屏幕截图 / screenshot）
- pyperclip（剪贴板操作 / clipboard）
- pillow（PIL，图像处理 / image processing）
- pyzbar（二维码识别 / QR code recognition）
- opencv-python（调试用图像保存 / debug image saving）
- numpy（图像数组转换 / array conversion）

---

## 注意事项 | Notes

- 首次运行如遇权限问题，请授予屏幕录制权限。
- 若未识别到二维码，会在当前目录生成调试截图并自动删除。

- If you encounter permission issues on first run, please grant screen recording permission.
- If no QR code is detected, a debug screenshot will be saved and auto-deleted in the current directory.

---

## 截图 | Screenshot
![](screenshot.png)

