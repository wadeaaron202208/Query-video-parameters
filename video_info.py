from pymediainfo import MediaInfo
import tkinter as tk
from tkinter import filedialog

def main():
    # 弹出文件选择框
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(
        title="选择视频文件",
        filetypes=[("视频文件", "*.mp4;*.mkv;*.avi;*.mov;*.flv;*.wmv;*.webm"), ("所有文件", "*.*")]
    )

    if not filepath:
        print("未选择文件，程序退出。")
        return

    # 读取视频信息
    media_info = MediaInfo.parse(filepath)

    # 初始化变量
    video_bitrate = audio_bitrate = resolution = fps = video_codec = audio_codec = "未知"
    duration = 0

    for track in media_info.tracks:
        if track.track_type == "Video":
            video_codec = track.format
            resolution = f"{track.width}x{track.height}"
            fps = track.frame_rate
            video_bitrate = track.bit_rate
        elif track.track_type == "Audio":
            audio_codec = track.format
            audio_bitrate = track.bit_rate
        elif track.track_type == "General":
            duration = track.duration  # 毫秒

    # 单位转换
    duration_sec = float(duration) / 1000 if duration else 0
    if video_bitrate: video_bitrate = int(video_bitrate) / 1000  # kbps
    if audio_bitrate: audio_bitrate = int(audio_bitrate) / 1000  # kbps

    # 输出结果
    print("\n===== 视频文件信息 =====")
    print(f"文件路径: {filepath}")
    print(f"视频码率: {video_bitrate} kbps")
    print(f"音频码率: {audio_bitrate} kbps")
    print(f"视频时长: {duration_sec:.2f} 秒")
    print(f"分辨率: {resolution}")
    print(f"帧率: {fps} FPS")
    print(f"视频编码格式: {video_codec}")
    print(f"音频编码格式: {audio_codec}")

if __name__ == "__main__":
    main()
