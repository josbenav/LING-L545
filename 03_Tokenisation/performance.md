# Description of performance

To evaluate the performance of the algorithm, I used the maxmatch.py program with the 'original.test.txt' file, which has 200 Chinese sentences. Results from the maxmatch.py program were sent to the 'output.test.txt' file, using the following code: 
```
python3 maxmatch.py > output.test.txt
```
I will then run the program evaluate.py to evaluate the performance of the maxmatch.py algorithm. For this, I used the code below:
```
python3 evaluate.py output.test.txt tokenised.test.txt
```
Overall, the Word Error Rate in individual sentences ranges from 0.0% to 79.17% as the highest score, yet the majority of sentences have less than 50%. 

Two examples of each follow: 

WER: 0.00%
REF: 從 20 世紀 60 年代 初 就 定居 下來 的 伊斯蘭 市民 主要 來 自 土耳其 。 
HYP: 從 20 世紀 60 年代 初 就 定居 下來 的 伊斯蘭 市民 主要 來 自 土耳其 。 
EVA:  

WER: 79.17%
REF: D u r á n     擔任 發言人 ， Á n g e l P i n t a d     o       擔任 財務 長   。 
HYP:         Durán 擔任 發言人 ，                     Ángel Pintado 擔任    財務長 。 
EVA: D D D D S              D D D D D D D D D D S     S          D  S     
(Note that the error rate comes from the names)

WER: 26.83%
REF: 公元 前 4 9  年 1 月 1 日 ， 馬克 · 安 東 尼   宣布 了 一 封 來 自 凱 撒  的 宣 言  ， 其中 表示 地方 總督 宣布 和 他 建立 和平 的 友 誼  關係 。 
HYP: 公元 前   49 年 1 月 1 日 ， 馬克 ·     安東尼 宣布 了 一 封 來 自   凱撒 的   宣言 ， 其中 表示 地方 總督 宣布 和 他 建立 和平 的   友誼 關係 。 
EVA:      D S                   D D S                D S    D S                               D S  

The average Word Error Rate and the number of evaluated sentences are given below: 

Number of sentences: 200
Average WER: 35.59%

Find all the results from the performance in the 'tokenized.test.results.txt' file. 