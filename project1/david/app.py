from flask import Flask, render_template, request
from gtts import gTTS
from io import BytesIO
import base64
import os
from datetime import datetime

app = Flask(__name__, template_folder='templates', static_folder='static')
DEFAULT_LANG = os.getenv("DEFAULT_LANG", "ko")
LOG_FILE = 'input_log.txt'

def log_input(text, lang):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f"[{timestamp}] lang={lang}, input={text}\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    audio = None
    audio_filename = None

    if request.method == 'POST':
        text = request.form.get('input_text', '').strip()
        lang = request.form.get('lang', DEFAULT_LANG)

        if not text:
            error = '텍스트를 입력해주세요.'
        else:
            try:
                tts = gTTS(text=text, lang=lang, tld='com')
                fp = BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)
                audio_bytes = fp.read()

                audio = base64.b64encode(audio_bytes).decode('utf-8')
                audio_filename = 'tts_output.mp3'

                log_input(text, lang)

            except ValueError as ve:
                error = f"언어({lang})에 맞지 않는 문자가 포함되어 있을 수 있습니다."
            except Exception as e:
                error = f"음성 변환 실패: {str(e)}"


    return render_template('index.html', error=error, audio=audio, audio_filename=audio_filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
