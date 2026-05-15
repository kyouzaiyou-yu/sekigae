import random
past = list(range(0,45))
#44,34,26,37が最前列なので除去
past.remove(44)
past.remove(34)
past.remove(26)
past.remove(37)
list_after = random.sample(past,len(past)) #random.sample(リスト,要素数)でリストを要素数分並びかえ
list_after = [44,34,26,37]+list_after #最前列指定の文を追加
list_c = list() #列ごとのlist
for index,i in enumerate(list_after):
    if index % 6 ==0 and index != 0: #index mod 6つまり六回ごと(1列文)に実行
        string = "" #stringという列ごとの出力の初期化
        for j in list_c: #列ごとのlist_cをjに1つづつ代入し実行
            string = string + f"{j:02d} " # "## "二桁の数スペースというフォーマットで追加  
        print(string) #列ごとの出力
        list_c = list() #新しいい列の初期化
    if index < 42: #42席分indexが41の時まで実行
        list_c.append(i) #列ごとのリストに要素を追加
    else: #42席以上いったら
        break #forループから抜け出す
string = f"      {list_after[42]:02d} {list_after[43]:02d} {list_after[44]:02d}   " #残りの席用のフォーマット
print(string) #残りの席を出力
