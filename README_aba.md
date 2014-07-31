#実行方法(2パターン)


##プログラムの機能

*排出の検知(LED)

*自動メール送信

-------


##準備

1. home/pi/Desktop/にworkフォルダ作成

2. workにaba_test.py,detect_mail.txtの２つを保存

3. detect_mail.txtのTOのアドレスを送信先のアドレスに変更

### メールサーバーの設定

ssmtpを使用します

 1.ssmtpのインストール
 
 `sudo apt-get install ssmtp`


全部yで


 2. 設定の編集
 
 `sudo vi /etc/ssmtp/ssmtp.conf` を開き

 以下のコマンドを入力

mailhub=smtp.gmail.com:587  

AuthUser=[gmailのメールアドレス]

AuthPass=[gmailのパスワード]

AuthMethod=LOGIN

UseSTARTTLS=YES

UseTLS=Yes


> 参考 Linuxブログ : ラズベリーパイ(raspbian)を使ってみる – 5分でメールを送信できるようにする - http://bit.ly/VTYJwV


#手動で実行

１分毎にscvファイルに書き込まれ１時間で保存

`sudo python aba_test.py`



##自動実行(1時間ごと)

### 1. ラズベリーの時間の設定(手動です)

コマンド : `sudo date -s "08/01 8:00 2014"`

> 現在時刻に修正して入力



### 2. cron設定（プログラムを自動実行にする）

*毎時０分になるとプログラム実行されます

コマンド: `crontab -e`

末尾に書き足す→  `00 * * * * cd ~/Desktop/work; sudo python aba_test.py`

> aba_test.pyを置いているディレクトリを指定

