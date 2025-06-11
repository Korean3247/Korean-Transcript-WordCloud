````markdown
# Korean-Transcript-WordCloud

Generate clean, high-resolution word-cloud images from Korean transcripts in **one command**.  
The script combines `KoNLPy`-Okt stemming, custom stop-word filtering, frequency scaling, and
optional per-word boosting (e.g., *“주차”, “자가용”*). Perfect for interview / FGI transcripts,
policy workshops, or any large block of Korean text.

<p align="center">
  <img src="wordcloud_output.png" width="450" alt="Sample word-cloud">
</p>

---

## ✨  Features
- **Accurate Korean tokenization** with `Okt` and stem normalization  
- **Noise removal**: interjections, endings, particles → regex pre-processing  
- **Smart stop-word list** (easily extendable)  
- **Per-word boost** to spotlight key terms  
- **Frequency smoothing** (√-scaling by default) to control oversized words  
- Outputs **800×800 px PNG** (DPI 300) ready for reports & slides  

---

## 🛠  Requirements
| Package | Tested Version |
|---------|---------------|
| Python 3.9+ | |
| konlpy | 0.6.0 |
| wordcloud | 1.9.3 |
| matplotlib | 3.9.0 |

> **Font** – place a Korean TTF (e.g., `NanumGothic.ttf`) in the project root or update the path.

Install all deps:

```bash
pip install konlpy wordcloud matplotlib
````

macOS/Linux users may need:

```bash
sudo apt-get install g++                     # Ubuntu
brew install openjdk                         # macOS
export JAVA_HOME=$(/usr/libexec/java_home)   # macOS
```

---

## 🚀  Usage

```bash
python wordcloud_maker.py \
    --input recording_transcript(2).txt \
    --font NanumGothic.ttf \
    --output wordcloud_output.png
```

*No CLI yet?*
Just edit the filenames at the top of **`wordcloud_maker.py`** and run:

```bash
python wordcloud_maker.py
```

The image will open in a matplotlib window and save to `wordcloud_output.png`.

---

## ⚙️  Customisation

| Task                         | How                                               |
| ---------------------------- | ------------------------------------------------- |
| **Add/modify stop-words**    | Update the `stopwords` list (section #4).         |
| **Highlight specific words** | Edit `boost_words` dict (section #7).             |
| **Limit max font size**      | Change `max_font_size` in the `WordCloud()` call. |
| **Adjust frequency scaling** | Tweak the exponent in `count**0.7` (0.5 ≦ x ≦ 1). |

---

## 🤝  Contributing

1. Fork → Commit message in English or Korean
2. Run `pre-commit run --all-files` (optional)
3. Pull-request to `main`

Bug-reports and feature requests welcome via Issues 💬.

```
