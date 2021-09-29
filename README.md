# Dcard Crawler 爬蟲程式

有鑒於Dcard於更新後增加許多爬蟲的限制，本程式使用[PTT Brain](https://www.pttbrain.com/)上的Dcard版進行爬蟲。

## 開始使用
1. 請先於終端機上下載本repo：
```sh
git clone https://github.com/enjuichang/Dcard-Crawler.git
```
2. 安裝`selenium`：請記得安裝`selenium`套件，以及下載`chromedriver`。如有更多疑問請觀看**Tech with Tim**的[教學影片](https://www.youtube.com/watch?v=Xjv1sY630Uc)。
3. 請更改`URLs`變數：
    - `URLs`變數預設為List of lists，每一個list對應到`labelLIST`中一個標籤（例如：\[\[A,B\],\[C,D\]\]中，A與B版將對應到一個標籤而C與D版則是另一個標籤。）
    - 如果將進行監督式學習的資料庫，請同時更改`URLs`與`labelLIST`，並且兩者長度相同（`len(URLs)==len(labelLIST)`）
    - 如果只是純粹爬蟲請將`labelLIST`留下`NA`（`labelLIST = [np.nan]`）並在`URLs`只使用一個`list`（`URLs = [[A,B,C,D]]`）(*未來將為非監督式學習建立方程式*)
4. 更改Output檔名：請於`df.to_csv`處更改儲存檔名，檔案將儲存於`~/csv/`
5. 執行程式

## English Version
Due to the inaccessibility of crawling Dcard after the new update, this program scrapes the data from [PTT Brain](https://www.pttbrain.com/), which has the top 200 posts for each tags on Dcard.

## Getting Started
1. Clone this repo to your local computer：
```sh
git clone https://github.com/enjuichang/Dcard-Crawler.git
```
2. Install `selenium`：Remeber to install `selenium` package and remember to install `chromedriver`. If there are any further questions, please refer to [this tutorial](https://www.youtube.com/watch?v=Xjv1sY630Uc) from **Tech with Tim**.
3. Change `URLs` variable:
    - `URLs` is set to default as a List of lists, which each list corresponding to a label in `labelLIST` (e.g.,In \[\[A,B\],\[C,D\]\]，A and B tags corresponds to one tag, while C and D corresponds to another.)
    - If the crawler is for supervised learning, please change `URLs` and `labelLIST` accordingly with the lengths of the two lists exactly identitical (`len(URLs)==len(labelLIST)`).
    - If supervised learning is not applicable, please leave `labelLIST` with `NA` (`labelLIST = [np.nan]`) and include only one `list` in `URLs` (`URLs = [[A,B,C,D]]`)(*Future updates will include function for only extracting the text*)
4. Change Output name: Please change the file name for the output at `df.to_csv`. The file will be saved in `~/csv/`.
5. Run program.
