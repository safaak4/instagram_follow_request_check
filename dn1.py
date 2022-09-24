from webbot import Browser
import time

atilan_takip_istekleri = [

"ahmetmehmet",
"12 Tem 2016 14:47",
"sedaaylin"
"12 Tem 2016 14:49",

] #instagramdan aldığınız html dosyasındakileri kopyalayıp bu list'e yapıştıracaksınız.


web = Browser()

isletmekullaniciadi = "dürümcümemo" #İşletmenizin kullanıcı adını buraya girin
isletmesifresi = "dürümcümemo123" #İşletmenizin şifresini buraya girin

web.go_to('instagram.com')
web.type(isletmekullaniciadi, into="username")
web.type(isletmesifresi, into="password")
web.click('Log In')

i = 1
while i <= len(atilan_takip_istekleri)/2:

    time.sleep(5)
    web.go_to("instagram.com/" + str(atilan_takip_istekleri[i * 2 - 2]))
    time.sleep(3)
    web.click('Requested', multiple = True)
    time.sleep(1)
    web.click("Unfollow")

    i = i + 1
