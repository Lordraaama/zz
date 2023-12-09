from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_watermark(video_path, watermark_text):
    video_clip = VideoFileClip(video_path)

    watermark_clip = TextClip(watermark_text, fontsize=40, color='white', bg_color='black', size=(video_clip.size[0], 50))
    watermark_clip = watermark_clip.set_position(('center', 10)).set_duration(video_clip.duration)

    watermarked_clip = CompositeVideoClip([video_clip, watermark_clip])

    output_path = "watermarked_video.mp4"
    watermarked_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)

    return output_path
