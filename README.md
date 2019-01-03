(2018年度文化祭)似ている芸能人診断ver2.0マニュアル

動作環境(確認済み)
mac      :10.13.6
anaconda :5.1.0
python   :3.5.6
chainer  :5.0.0

1. 皆さんの開発環境と衝突するといけないので、knfと言う名前で（違う名前でもいいです）新しく仮想環境を構築します。
ターミナルで以下の順で実行。
conda create -n knf python=3.5
source activate knf（windowsの場合はactivate knf）
conda install chainer
pip install chainercv
pip install opencv-python

2. git clone https://github.com/take-r/Similar_person.git
を実行

3. cd Similar_person

4. python main_2_0.py

5. PC内蔵カメラが起動するので、カメラのウィンドウを選択した後に何らかのボタンを押すと撮影（この際、できるだけ中央に顔が来るようにして撮影してください）

6. 結果が表示されます。以降は手順４以降を繰り返し。

*診断の元になっている有名人の顔写真はpictureフォルダ内にあります。