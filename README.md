似ている芸能人診断ver2.0マニュアル

1. 皆さんの開発環境と衝突するといけないので、knfと言う名前で（名前は何でもいいです）新しく仮想環境を構築します。
conda create -n knf python=3.5
source activate knf（windowsの場合はactivate knfかも）
conda install chainer
pip install chainercv
pip install opencv-python

2.slackからmain_2_0.py, resnet50_128.caffemodel, vec_list.txtを同じフォルダにダウンロード
resnet50_128.caffemodelはhttps://github.com/ox-vgg/vgg_face2 からダウンロードお願いします。

3.main_2_0.pyのline12にあるdata_folderを、保存したフォルダのディレクトリに変える。保存

4.ターミナルでmain_2_0.pyを実行

5. PC内蔵カメラが起動するので、ウィンドウを選択した後に何らかのボタンを押すと撮影（この際、できるだけ中央に顔が来るようにして撮影してください）

6. 結果が表示されます。以降は手順４以降を繰り返し。


＊男女両方の芸能人を登録しました。異性の名前が表示されることが多々あります。
*githubの使い方をあまり分かっていないため、データファイルをそのまま載せただけになります。未熟で申し訳ありません。
