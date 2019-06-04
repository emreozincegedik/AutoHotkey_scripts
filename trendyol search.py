import requests
from bs4 import BeautifulSoup

isim=input("Lutfen aramak istediginiz urunu giriniz: ") 
site=requests.get("https://www.trendyol.com/tum--urunler?q="+isim+"&st="+isim+"&qt="+isim+"&qs=search")
html_kodu =site.content #içeriğini alıyoruz
islenmis_html=BeautifulSoup(html_kodu,features="html.parser") 

urun_isimleri=islenmis_html.find_all('span', attrs={'class':'prdct-desc-cntnr-name'}) 
urun_fiyatlari=islenmis_html.find_all('div', attrs={'class':'prc-box-sllng'}) 

urun_linkleri=islenmis_html.find_all('a',attrs={'class':'p-card-chldrn-cntnr'}) 
i=1
for isim,fiyat in zip(urun_isimleri,urun_fiyatlari):  #döngüye sokup ürün numarası, ismi ve fiyatlarını yazdırıyoruz
  print(str(i)+". "+str(isim.attrs['title'])+" "+ str(fiyat.text)) #yazdırma işlemi
  i+=1 

istek=input("Hangi ürünün yorumunu görmek istiyorsunuz? ") #hangi yorum isteniyor

while True: #istek düzgün mü kontrol
  while not istek.isdigit(): #istek sayı mı
    istek=input("Lütfen düzgün istek giriniz: ") #değilse tekrar istek
  if  int(istek)<1 or int(istek)>len(urun_isimleri): #sayı ürün sayısından fazla ya da 1den küçükse başa döndürtüyoruz
    istek="g" #istek düzgün değil olarak güncelliyoruz
    continue
  break #hepsini geçerse döngüden çıkıyor

sayi=int(istek)-1 #istek 1 ise 0. elemanda çalışmalıyız
k=urun_linkleri[sayi].get('href') #linkler arasındaki sayınıncı elemanın gönderdiği linki çekiyoruz
kacinci_urun=requests.get("https://www.trendyol.com"+k) #linkten çek
html_kacinci_urun=kacinci_urun.content #linkin içeriğini al
islenmis_html_kacinci_urun=BeautifulSoup(html_kacinci_urun,features="html.parser") #html olduğunu belirt
yorumlar=islenmis_html_kacinci_urun.find_all('p', attrs={'class':'rnr-com-tx'}) #yorumları .ek
print(str(urun_isimleri[sayi].attrs['title'])+" "+str(urun_fiyatlari[sayi].text)) #istenilen ürünün ismi ve parasını tekrar yazdır
for t in yorumlar: #yorumlar için döngüye girdiriyoruz
  print(t.text) #her yorumu yazdır


