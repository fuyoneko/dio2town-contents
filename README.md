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

## Lisence

MIT
