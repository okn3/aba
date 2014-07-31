#実行方法(2パターン)


##プログラムの機能

*排出の検知(LED)

*自動メール送信

-------


##準備

1. home/pi/Desktop/にworkフォルダ作成

2. workにaba_test.py,detect_mail.txtの２つを保存

3. detect_mail.txtのTOのアドレスを送信先のアドレスに変更

#手動で実行

１分毎にscvファイルに書き込まれ１時間で保存

`sudo python aba_led_mail.py`



#自動実行(1時間ごと)

1. ラズベリーの時間の設定

コマンド : `sudo date -s "08/01 8:00 2014"`

> 修正して入力


2. cron設定（プログラムを自動実行にする）

コマンド: `crontab -e`

末尾に書き足す→  `00 * * * * cd ~/Desktop/work; sudo python aba_test.py`

> aba_test.pyを置いているディレクトリを指定

