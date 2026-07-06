import time
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode
import pyperclip

# Tracking parameters we want to strip from URLs
TRACKING_PARAMS = {
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
    'fbclid', 'gclid', 'msclkid', 'twclid', 'si'
}

def clean_url(text):
    try:
        parsed = urlparse(text)
        # If it doesn't look like a URL, don't mess with it
        if not parsed.scheme or not parsed.netloc:
            return text
            
        # Parse query string, filter out tracking junk, and rebuild
        query_params = parse_qsl(parsed.query)
        cleaned_params = [(k, v) for k, v in query_params if k.lower() not in TRACKING_PARAMS]
        
        new_query = urlencode(cleaned_params)
        return urlunparse(parsed._replace(query=new_query))
    except Exception:
        return text

def clean_text(text):
    if not text:
        return ""
        
    trimmed = text.strip()
    
    # Handle URLs specifically, otherwise just fix messy whitespace
    if trimmed.startswith(('http://', 'https://')):
        return clean_url(trimmed)
    
    # Cleans up weird multi-line spacing but keeps normal paragraphs
    lines = [line.strip() for line in trimmed.splitlines()]
    return '\n'.join(line for line in lines if line)

def main():
    print("Clipboard cleaner running... Press Ctrl+C to stop.")
    last_text = pyperclip.paste()
    
    try:
        while True:
            current_text = pyperclip.paste()
            
            if current_text != last_text:
                cleaned = clean_text(current_text)
                
                if cleaned != current_text:
                    pyperclip.copy(cleaned)
                    print("Cleaned up copied text.")
                    # Update last_text with the cleaned version so we don't trigger again
                    last_text = cleaned
                else:
                    last_text = current_text
                    
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nStopping clipboard cleaner.")

if __name__ == "__main__":
    main()
