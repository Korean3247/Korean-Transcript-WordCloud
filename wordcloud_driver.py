# Install required libraries:
# pip install konlpy wordcloud matplotlib

from konlpy.tag import Okt
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

# 1. Load the text data
with open('recording_transcript(2).txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Preprocessing: remove filler words, endings, and particles
text = re.sub(r'[음아어]+', ' ', text)  # remove interjections (e.g., "음", "아", "어")
text = re.sub(r'\b(요|죠|네|는데|지만|같이|정도|그런데|그럼|일단)\b', ' ', text)  # remove common endings/particles
text = re.sub(r'\s+', ' ', text)  # normalize whitespace

# 3. Morphological analysis with stemming
okt = Okt()
words = okt.pos(text, stem=True)

# 4. Define stopword list (general + custom)
stopwords = list(set([
    # General stopwords
    '이제', '그건', '그거', '이건', '그런', '그렇다', '여기', '거기', '정도', '얘기',
    '사람', '저희', '자기', '직접', '생각', '사실', '때문', '정말', '그냥', '항상',
    '그렇죠', '같이', '그게', '누가', '누구', '다시', '근데', '아마', '어차피',
    '일단', '그럼', '요즘', '우리', '본인', '자신', '뭔가', '언제', '아예', '계속',
    '그렇고', '아니면',

    # Context-specific noise words
    '말씀', '경우', '하나', '지금', '내용', '내요', '시스템', '신청', '자차', '배려',
    '병원', '요소', '대상', '지원', '이용', '정보', '제도', '예약', '안내', '구매',
    '공간', '운영', '수요', '혜택', '체감', '시간', '상황', '가치', '그것', '가장',
    '제일', '보통', '한번', '주신', '쯤', '엄마', '애', '미리', '가야', '해야', '거냐',
    '실질', '보고', '기차', '수단', '지역', '주로', '그것도', '그때', '확보', '정도', '좀', '거의',
    '조금', '약간', '개월', '확인', '대부분', '데리', '가면', '혹시', '이상', '한해', '대해', '조금',
    '부분', '진짜', '다른', '설명', '차라리', '하여튼', '대한', '거나', '대로'
]))

# 5. Filter: nouns only, remove stopwords, length ≥ 2
filtered_words = [
    word for word, tag in words
    if tag == 'Noun' and word not in stopwords and len(word) > 1
]

# 6. Count word frequencies
word_counts = Counter(filtered_words)

# 7. Boost frequency for key words
boost_words = {'주차': 15, '자가용': 15}  # emphasize these words

for word, boost in boost_words.items():
    if word in word_counts:
        word_counts[word] += boost

# 8. Frequency scaling (optional): square-root-like scaling to reduce gap
scaled_counts = {word: count**0.7 for word, count in word_counts.items()}  # adjust 0.5–1.0 as needed

# 9. Get top-N frequent words
top_words = dict(Counter(scaled_counts).most_common(100))

# 10. Generate the word cloud
wordcloud = WordCloud(
    font_path='NanumGothic.ttf',
    width=800,
    height=800,
    background_color='white',
    max_font_size=180
).generate_from_frequencies(top_words)

# 11. Display and save the image
fig = plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
fig.savefig("wordcloud_output.png", dpi=300)  # high-resolution PNG
plt.show()
