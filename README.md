# Korean Transcript WordCloud

**Program Title**
Korean Word Cloud Generator from Transcripts

**Description**
This Python program processes Korean text—especially from interview transcripts or policy recordings—and generates a word cloud by analyzing noun frequencies. It uses the KoNLPy library for morphological analysis, removes common filler words and particles, applies custom stop-word filtering, and emphasizes specified keywords visually.

**How It Works**
The program reads a `.txt` file containing Korean text and performs the following steps:

1. Removes filler words and unnecessary particles via regex.
2. Analyzes the text using the `Okt` morphological analyzer with stemming.
3. Filters out common or domain-specific stopwords.
4. Applies optional keyword boosting to emphasize terms (e.g., "주차", "자가용").
5. Scales word frequencies for better visual balance.
6. Generates a word cloud image and saves it as a high-resolution PNG file.

**Input Requirements**

* Input Text File: A `.txt` file containing Korean text (UTF-8 encoding).
* Font File: A Korean TTF font file (e.g., `NanumGothic.ttf`) in the same directory.

**Features**

* KoNLPy-based noun extraction and normalization.
* Easily extensible stop-word list.
* Boost specific words for emphasis in visualization.
* Adjustable frequency scaling to avoid oversized dominant words.
* Saves output as a clean 800×800 high-DPI image.

**Usage Example**

```
Check the name of your text file and update the path inside wordcloud_maker.py, then run the following:
python wordcloud_maker.py
```

The output image `wordcloud_output.png` will appear in the same folder.

**Files**

* `wordcloud_maker.py`: The main Python script.
* `recording_transcript(2).txt`: Example input transcript.
* `NanumGothic.ttf`: Korean font file for proper rendering.
* `wordcloud_output.png`: The generated image (output).

**System Requirements**

* Python 3.x
* Libraries: `konlpy`, `wordcloud`, `matplotlib`
* Korean-compatible font (e.g., NanumGothic)

**How to Run**

1. Install required packages:

   ```bash
   pip install konlpy wordcloud matplotlib
   ```
2. Place your `.txt` input and `.ttf` font in the same directory as the script.
3. Run the script:

   ```bash
   python wordcloud_maker.py
   ```
4. View the output image `wordcloud_output.png`
