import yt_dlp
import json

def search_ok_ru(query, max_results=5):
    # আমরা সরাসরি OK.RU এর ভিডিও সার্চ ইউআরএল ব্যবহার করছি
    search_url = f"https://ok.ru/video/search?st.query={query}"
    
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # ভিডিও সার্চ করা
            result = ydl.extract_info(search_url, download=False)
            
            video_list = []
            if 'entries' in result:
                # OK.RU এর সার্চ রেজাল্ট থেকে ভিডিওগুলো নেওয়া
                for entry in result['entries'][:max_results]:
                    if entry:
                        video_data = {
                            "title": entry.get("title"),
                            "url": entry.get("url") if entry.get("url") else f"https://ok.ru/video/{entry.get('id')}",
                            "thumbnail": entry.get("thumbnail"),
                            "id": entry.get("id")
                        }
                        video_list.append(video_data)
            
            return video_list
        except Exception as e:
            print(f"Error occurred: {e}")
            return []

# সার্চ কীওয়ার্ড দিন
keyword = "Buddy (2024) Hindi Dubbed"
videos = search_ok_ru(keyword)

if videos:
    # ডেটা JSON ফাইলে সেভ করা
    with open('ok_videos.json', 'w', encoding='utf-8') as f:
        json.dump(videos, f, ensure_ascii=False, indent=4)
    print(f"Successfully saved {len(videos)} videos to ok_videos.json")
else:
    print("No videos found or error occurred.")
