import os

print("現在のフォルダ:", os.getcwd())
print("保存先:", os.path.abspath("todo.csv"))

while True:
     import csv
     print('1新規作成or2確認or3修正or0終了' )
     A = input()
     if A in ['新規作成' , '1' , '新規' , '作成']:
          print('タイトル、概要、締め切り、優先度 を記入して')
          B = input().split()
          print('title:',B[0],end=" ")
          print('概要：',B[1])
          print('締め切り：',B[2])
          print('優先度：',B[3])
          with open("todo.csv", "a",newline="",encoding="utf-8") as f:     #箱開けて
        #ファイル名、追加()、出力先の縦改行 空白なくす、文字化け用、）これをｆとする
           
         #f.write(f"タイトル: {B[0]}\n")
         #f.write(f"概要: {B[1]}\n")
         #f.write(f"締め切り: {B[2]}\n")
         #f.write(f"優先度: {B[3]}\n")
         #f.write(f"タイトル:{B[0]},概要：{[1]},締め切り：{B[2]},優先度：{B[3]}")2
           writer = csv.writer(f)  #ｆを実際のファイルに書き込み 　　　　土台置いて
           writer.writerow(B)    #ファイルに保存　　　　　　　　　　　　　実際に書く
           print('保存しました')
           
           
     if A in ['確認' , '2']:          #確認
          key = input('タイトルを記入して').strip()
          
          if key in ['全部' , 'all']:
               with open("todo.csv","r",encoding="utf-8") as f:
                    reader = csv.reader(f) #ファイルから引き出す

                    priority = {"高" : 0,"中" : 1,"低" : 2}

                    reader_list = list(reader)
                    reader_list.sort(key=lambda row: priority[row[3]])  # 1.2(2は動作)   2=1   3=1.2  〇:制約　〇.動作  lambda=一行だけ取って

                    for row in reader_list:
               
                    
                         print(f'title:{row[0]} 概要:{row[1]} 締め切り:{row[2]} 優先度:{row[3]}')
                    
          else:
               found = False

               with open("todo.csv","r",encoding="utf-8") as f:
                    reader = csv.reader(f) #ファイルから引き出す
                    
                    for row in reader:
                        if key == row[0]:
                              print(f'title:{row[0]} 概要:{row[1]} 締め切り:{row[2]} 優先度:{row[3]}') #書式指定
                              
                              found = True
                              break

               if not found:
                    print('該当するリストが見つかりません')
          
          
     if A in ['修正', '編集', '3']:
       key2 = input('タイトルを記入して')
       with open("todo.csv","r",encoding="utf-8") as f:
          reader = csv.reader(f) #ファイルから引き出す
          
          rows = []

          for row in reader:
               if key2 == row[0]:
                    print('title:',row[0])
                    print('概要：',row[1])
                    print('締め切り：',row[2])
                    print('優先度：',row[3])

                    print('タイトル、概要、締め切り、優先度 を記入して')
                    new = input().split()
                    
                    row[0] = new[0]
                    row[1] = new[1]
                    row[2] = new[2]
                    row[3] = new[3]

                    print('新しいタイトル:',new[0])
                    print('新しい概要：',new[1])
                    print('新しい締め切り：',new[2])
                    print('新しい優先度：',new[3])
                    
               rows.append(row)
               
               
          with open("todo.csv","w",newline="",encoding="utf-8") as f:
               writer = csv.writer(f)
               writer.writerows(rows)

          print('修正しました')


     if A in ('0 or 終了'):
          break

