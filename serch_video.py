import yt_dlp
import json

def search_ok_ru(query, max_results=5):
    # Search command for OK.ru
    search_url = f"oksearch:{query}"
    
    ydl_opts = {
        'quiet': True,
        'extract_flat': True, # শুধু তথ্য নেবে, ভিডিও ডাউনলোড করবে না
        'force_generic_extractor': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # ভিডিও সার্চ করা
        result = ydl.extract_info(search_url, download=False)
        
        video_list = []
        if 'entries' in result:
            for entry in result['entries'][:max_results]:
                video_data = {
                    "title": entry.get("title"),
                    "url": entry.get("url"),
                    "thumbnail": entry.get("thumbnail"),
                    "id": entry.get("id")
                }
                video_list.append(video_data)
        
        return video_list

# সার্চ কীওয়ার্ড দিন (যেমন: Live Streaming বা কোনো নাম)
keyword = "Buddy (2024) Hindi Dubbed"
videos = search_ok_ru(keyword)

# ডেটা JSON ফাইলে সেভ করা
with open('ok_videos.json', 'w', encoding='utf-8') as f:
    json.dump(videos, f, ensure_ascii=False, indent=4)

print("OK.RU ভিডিওর তথ্য ok_videos.json ফাইলে সেভ হয়েছে!")
