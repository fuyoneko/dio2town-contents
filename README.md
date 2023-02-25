# Dio2TownContents

## Overview

Dio2Town のサンプルデータです

## What is Dio2Town

Draw.io で作成したデータを、3D に変換して自由に操作できるライブラリです  
デジタルツインに利用することも、地図コンテンツとして利用することもできます

## How to use

website/index.html を参照してください

## Development

### Web サーバを起動する

website ディレクトリでサーバを立てることで起動します

例：Python でサーバを立てる場合

```bash
cd website
python -m http.server
```

### 3D データをパッケージングする

3D 上では、バンドルした glb ファイルの 3D オブジェクトを表示できます

バンドルには以下のコマンドを利用します

```bash
cd 3d_resource
python convert.py
```

## Relationship

Draw.io のデータを変換するライブラリは以下のレポジトリで管理しています

Dio2Town

https://github.com/fuyoneko/dio2town

## Demo

Draw.io を Google Drive に保存して、Wiki のように複数人で編集することができます  
以下の URL からデモを触ることができます

> ※Draw.io の編集には Google アカウントの認証が必要です。認証では全権限をチェックしてください  
> 編集した内容はリアルタイムで閲覧用ページに反映されます

### おためしサンドボックス（※自由に編集していただいて大丈夫です）

**[Draw.io の編集用ページ]**

https://drive.google.com/file/d/10CCJCN-9HwU1zZrE__E6LSnfIyDsBWfd/edit?usp=sharing

**[3D 地図の閲覧用ページ]**

https://fuyoneko.github.io/dio2town-contents/sandbox/

### 検証用プロジェクト（※大阪市西成区山王町の地図です。現地の情報にあった編集をお願いします）

**[Draw.io の編集用ページ]**

https://drive.google.com/file/d/1eQg0szn6TCXxgg0Ddr6eHIsIlyEeINPO/edit?usp=sharing

**[3D 地図の閲覧用ページ]**

https://fuyoneko.github.io/dio2town-contents/tobitamap/

## Lisence

MIT
