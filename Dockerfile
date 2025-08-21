FROM python:3.10-slim


RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc g++ make && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .


RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt


ENV NLTK_DATA=/usr/local/share/nltk_data
RUN mkdir -p "$NLTK_DATA" && \
    python - <<'PY'
import nltk
nltk.download('vader_lexicon', download_dir='/usr/local/share/nltk_data')
nltk.download('punkt', download_dir='/usr/local/share/nltk_data')
PY


COPY . .


RUN useradd -m appuser
USER appuser


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers","4"]