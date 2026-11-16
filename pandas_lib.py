"""
Pandas: Veri bilimi kütüphanesi
    - Tablo şeklinde veri oluşturmak
    - verileri düzenlemek, filtrelemek
    - sütun ve satır isimleri yapmak
    - dosyalardan veri okumak

Pandas Numpy ilişkisi:
    - Numpy sayısal dizi sağlar
    - pandas: tablo veri yapıları

Pandas nerelerde kullanılır?
    - veri analizi
    - veri düzenleme
    - veri temizleme
    - veri işleme
    - veri dosyalarını okuma

Pandas ile ilgili neler öğreneceğiz?
    - Series
    - dataframe
    - veri okuma ve yazma
    - veri seçme ve filtreleme
    - sütun ve satır işlemleri
    - veri sıralama ve gruplama
    - temel pandas fonksiyonları
"""
import pandas as pd

"""
Series
"""
# series oluşturma
veri = pd.Series([10, 20, 30, 40])
print(veri)
"""
index    value
0        10        
1        20
2        30
3        40

key-value (dict)
index-value (pandas series)
0: 10        
1: 20
2: 30
3: 40
"""

# series içindeki verilere erişme
veri = pd.Series([10, 20, 30, 40])
print(veri[0]) # 10
print(veri[2]) # 30

# series için özel indeks belirleme
veri = pd.Series([10, 20, 30], index = ["a", "b", "c"])
print(veri)
"""
a    10
b    20
c    30
"""
print(veri["b"]) # 20

# dictionary ile series oluşturma
veri = { # anahtar-value
    "ali": 80,
    "ayşe": 90,
    "mehmet": 75
}
s = pd.Series(veri)
print(s)
"""
index     value
ali       80
ayşe      90
mehmet    75
"""

# series özellikleri

print(s.index) # index  # Index(['ali', 'ayşe', 'mehmet'], dtype='str')
print(s.values) # değerleri  # [80 90 75]
print(s.dtype) # int64

# series ile matematiksel işlemler
veri = pd.Series([10, 20, 30, 40])
sonuc = veri * 2
print(sonuc) 

# series filtreleme
yas = pd.Series([10, 20, 30, 40, 50])
filtre = yas > 25 # boolean filtre
print(filtre)
"""
0    False
1    False
2     True
3     True
4     True
"""
sonuc = yas[filtre]
print(sonuc)

"""
dataframe
"""

# dataframe oluşturma
veri = {
    "isim":  ["mehmet", "selim", "süleyman"],
    "yas":   [21, 40, 35],
    "sehir": ["İstanbul", "Çaldıran", "Mohaç"]
}
df = pd.DataFrame(veri)
print(df)
"""
sütunlar: veri kategorileri
satırlar: her bir kayıt

       isim  yas     sehir
0    mehmet   21  İstanbul
1     selim   40  Çaldıran
2  süleyman   35     Mohaç
"""

# sütun isimleri
print(df.columns) # Index(['isim', 'yas', 'sehir'], dtype='str')

# dataframe satır sayısı öğrenme
print(df.shape) # (3, 3)

# sütunlara erişim
print(df["isim"])

# birden fazla sütun seçme
print(df[["isim","yas"]])

# yeni sütun ekleme
df["maas"] = [5000, 7000, 6000]
print(df)
"""
       isim  yas     sehir  maas
0    mehmet   21  İstanbul  5000
1     selim   40  Çaldıran  7000
2  süleyman   35     Mohaç  6000
"""

# sütun silme
df = df.drop("sehir", axis = 1)
print(df)
"""
       isim  yas  maas
0    mehmet   21  5000
1     selim   40  7000
2  süleyman   35  6000
"""

# ilk satırları görüntülemek
print(df.head()) # ilk 5 satır

# son satırları görüntülemek
print(df.tail()) # son 5 satır

# dataframe hakkında bilgi alma
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    3 non-null      str  
 1   yas     3 non-null      int64
 2   maas    3 non-null      int64
dtypes: int64(2), str(1)
memory usage: 204.0 bytes
"""

"""
dosya okuma ve yazma
"""

# csv (comma separated values) dosyası okuma
df = pd.read_csv("veri.csv")
print(df)
"""
         isim   yas   not
0       berat    20    90
1        mert    25    95
2  değermenci    30    85
"""

# csv dosyası yazma
veri = {
    "isim": ["ali","ayse","mehmet"],
    "yas": [25, 30, 35]
}

df = pd.DataFrame(veri)

df.to_csv("veri_output.csv", index=False)

# excel dosyası yazma
df.to_excel("veri_output.xlsx",index=False)

"""
veri seçme ve filtreleme
"""

# örnek dataframe oluştur
veri = {
    "isim": ["ali", "ayse", "mehmet", "zeynep", "ahmet"],
    "yas": [25, 30, 28, 35, 22],
    "sehir": ["Ankara", "İstanbul", "İzmir", "Ankara", "Bursa"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}
df = pd.DataFrame(veri)
print(df)

# sütun seçme
print(df["isim"])

# birden fazla sütun seçme
print(df[["isim","maas"]])

# satır seçme: iloc
print(df.iloc[0])
"""
isim        ali
yas          25
sehir    Ankara
maas       5000
"""

# birden fazla satır
print(df.iloc[0:3])

# satır seçme: loc
print(df.loc[2])
"""
isim     mehmet
yas          28
sehir     İzmir
maas       6000
"""

# belirli bir satır ve belirli bir sütun
print(df.loc[:,["isim","maas"]])
"""
     isim  maas
0     ali  5000
1    ayse  7000
2  mehmet  6000
3  zeynep  8000
4   ahmet  4500
"""

print(df.loc[:2,["isim","maas"]])
"""
     isim  maas
0     ali  5000
1    ayse  7000
2  mehmet  6000
"""

# koşullu filtreleme
filtre = df["yas"] > 30
print(filtre)
"""
0    False
1    False
2    False
3     True
4    False
"""
sonuc = df[filtre]
print(sonuc)

print(df[df["yas"] > 30])
"""
     isim  yas   sehir  maas
3  zeynep   35  Ankara  8000
"""

# birden fazla koşul varsa
# sehir ankara ve maas 6000 den büyük olan insanları getir
sonuc = df[(df["sehir"] == "Ankara") & (df["maas"] > 6000)]
print(sonuc)
"""
     isim  yas   sehir  maas
3  zeynep   35  Ankara  8000
"""

# belirli bir değeri içeren satırlar
print(df[df["sehir"] == "Ankara"])
"""
     isim  yas   sehir  maas
0     ali   25  Ankara  5000
3  zeynep   35  Ankara  8000
"""

# sadece belirli sütunları gösterme
# yaşı 25 den büyük olan verinin sadece isim ve maaşını göster
print(df[df["yas"] > 25][["isim", "maas"]])
"""
     isim  maas
1    ayse  7000
2  mehmet  6000
3  zeynep  8000
"""

"""
sütun ve satır işlemleri
"""

# dataframe oluştur
veri = {
    "isim":["ali","ayse","mehmet"],
    "yas":[25, 30, 28],
    "maas":[5000, 2000, 6000]
}

df = pd.DataFrame(veri)
print(df)

# yeni bir sütun ekleme
df["sehir"] = ["trabzon","rize","artvin"]
print(df)

# hesaplama ile sütun oluşturma
df["yillik_maas"] = df["maas"] * 12
print(df)

# sütun silme
df = df.drop("maas", axis = 1)
print(df)

# sütun ismi değiştirme
df = df.rename(columns={"yillik_maas": "YillikMaas"})
print(df)

# yeni bir satır ekleme
df.loc[3] = ["zeynep",32,"giresun",80000]
print(df)

# satır silme
df = df.drop(0)
print(df)

# index değerlerini yeniden düzenleme
df = df.reset_index(drop=True)
print(df)

"""
veri sıralama ve gruplama
"""

# örnek dataframe oluştur
veri = {
    "isim":["murat","osman","orhan","bayazıd","mehmet"],
    "sehir":["ankara","istanbul","ankara","izmir","istanbul"],
    "maas":[5000,7000,8000,6000,4500]
}
df = pd.DataFrame(veri)
print(df)
"""
      isim     sehir  maas
0    murat    ankara  5000
1    osman  istanbul  7000
2    orhan    ankara  8000
3  bayazıd     izmir  6000
4   mehmet  istanbul  4500
"""
# veri sıralama
df_sirali = df.sort_values("maas")
print(df_sirali)
"""
      isim     sehir  maas
4   mehmet  istanbul  4500
0    murat    ankara  5000
3  bayazıd     izmir  6000
1    osman  istanbul  7000
2    orhan    ankara  8000
"""

# azalan sıralama
df_sirali = df.sort_values("maas",ascending=False)
print(df_sirali)
"""
      isim     sehir  maas
2    orhan    ankara  8000
1    osman  istanbul  7000
3  bayazıd     izmir  6000
0    murat    ankara  5000
4   mehmet  istanbul  4500
"""

# birden fazla sütuna göre sıralama
df_sirali = df.sort_values(["sehir","maas"])
print(df_sirali)
"""
      isim     sehir  maas
0    murat    ankara  5000
2    orhan    ankara  8000
4   mehmet  istanbul  4500
1    osman  istanbul  7000
3  bayazıd     izmir  6000
"""

# veri gruplama: groupby
# şehir bazında gruplama
gruplar = df.groupby("sehir")
print(gruplar) # <pandas.api.typing.DataFrameGroupBy object at 0x000002355BB4F620>

# grupların ortalama maaşı
sonuc = df.groupby("sehir")["maas"].mean() # şehir bazında ortalama maaş hesaplama
print(sonuc)
"""
ankara      6500.0
istanbul    5750.0
izmir       6000.0
"""

# grupların toplam maaşı 
sonuc = df.groupby("sehir")["maas"].sum()
print(sonuc)
"""
sehir
ankara      13000
istanbul    11500
izmir        6000
"""

# grupların kaç kişi olduğunu bulalım
sonuc = df.groupby("sehir")["isim"].count()
print(sonuc)
"""
sehir
ankara      2
istanbul    2
izmir       1
"""

# birden fazla işlem yapma
sonuc = df.groupby("sehir")["maas"].agg(["mean", "max", "min"])
print(sonuc)
"""
            mean   max   min
sehir                       
ankara    6500.0  8000  5000
istanbul  5750.0  7000  4500
izmir     6000.0  6000  6000
"""

"""
temel pandas fonksiyonları
"""

# örnek dataframe oluştur
veri = {
    "isim":["ali","ayse","mehmet","zeynep","ahmet"],
    "yas":[25, 30, 28, 35, 22],
    "sehir":["ankara","istanbul","ankara","izmir","istanbul"],
    "maas":[5000,7000,6000,8000,4500]
}
df = pd.DataFrame(veri)
print(df)
"""
     isim  yas     sehir  maas
0     ali   25    ankara  5000
1    ayse   30  istanbul  7000
2  mehmet   28    ankara  6000
3  zeynep   35     izmir  8000
4   ahmet   22  istanbul  4500
"""
# head fonksiyonu ile ilk 5 satırı görelim
print(df.head())

# tail ile son satırları görme
print(df.tail(3))

# info()
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    5 non-null      str  
 1   yas     5 non-null      int64
 2   sehir   5 non-null      str  
 3   maas    5 non-null      int64
dtypes: int64(2), str(2)
memory usage: 292.0 bytes
"""

# sayısal sütunların temel istatistiklerini görmek için describe()
print(df.describe())
"""
             yas         maas
count   5.000000     5.000000
mean   28.000000  6100.000000
std     4.949747  1431.782106
min    22.000000  4500.000000
25%    25.000000  5000.000000
50%    28.000000  6000.000000
75%    30.000000  7000.000000
max    35.000000  8000.000000
"""

# bir sütundaki değerlerin kaç kez tekrar ettiğini görmek için value_counts()
print(df["sehir"].value_counts())
"""
sehir
ankara      2
istanbul    2
izmir       1
Name: count, dtype: int64
"""
 
# bir sütundaki benzersiz değerleri görmek için unique fonksiyonunu kullanırız
print(df["sehir"].unique()) # ['ankara', 'istanbul', 'izmir']

# bir sütunda kaç farklı değer olduğunu görmek için nunique
print(df["sehir"].nunique()) # 3