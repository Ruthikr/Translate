import requests
import streamlit as st
import pandas as pd

languages={
"English":"en",
"Afrikaans":"af",
"Albanian":"sq",
"Amharic":"am",
"Arabic":"ar",
"Armenian":"hy",
"Azerbaijani":"az",
"Basque":"eu",
"Belarusian":"be",
"Bengali":"bn",
"Bosnian":"bs",
"Bulgarian":"bg",
"Catalan":"ca",
"Cebuano":"ceb",
"Chichewa":"ny",
"Chinese (Simplified)":"zh-CN",
"Chinese (Traditional)":"zh-TW",
"Corsican":"co",
"Croatian":"hr",
"Czech":"cs",
"Danish":"da",
"Dutch":"nl",
"Esperanto":"eo",
"Estonian":"et",
"Filipino":"tl",
"Finnish":"fi",
"French":"fr",
"Frisian":"fy",
"Galician":"gl",
"Georgian":"ka",
"German":"de",
"Greek":"el",
"Gujarati":"gu",
"Haitian Creole":"ht",
"Hausa":"ha",
"Hawaiian":"haw",
"Hebrew":"iw",
"Hindi":"hi",
"Hmong":"hmn",
"Hungarian":"hu",
"Icelandic":"is",
"Igbo":"ig",
"Indonesian":"id",
"Irish":"ga",
"Italian":"it",
"Japanese":"ja",
"Javanese":"jw",
"Kannada":"kn",
"Kazakh":"kk",
"Khmer":"km",
"Kinyarwanda":"rw",
"Korean":"ko",
"Kurdish (Kurmanji)":"ku",
"Kyrgyz":"ky",
"Lao":"lo",
"Latin":"la",
"Latvian":"lv",
"Lithuanian":"lt",
"Luxembourgish":"lb",
"Macedonian":"mk",
"Malagasy":"mg",
"Malay":"ms",
"Malayalam":"ml",
"Maltese":"mt",
"Maori":"mi",
"Marathi":"mr",
"Mongolian":"mn",
"Myanmar (Burmese)":"my",
"Nepali":"ne",
"Norwegian":"no",
"Odia (Oriya)":"or",
"Pashto":"ps",
"Persian":"fa",
"Polish":"pl",
"Portuguese":"pt",
"Punjabi":"pa",
"Romanian":"ro",
"Russian":"ru",
"Samoan":"sm",
"Scots Gaelic":"gd",
"Serbian":"sr",
"Sesotho":"st",
"Shona":"sn",
"Sindhi":"sd",
"Sinhala":"si",
"Slovak":"sk",
"Slovenian":"sl",
"Somali":"so",
"Spanish":"es",
"Sundanese":"su",
"Swahili":"sw",
"Swedish":"sv",
"Tajik":"tg",
"Tamil":"ta",
"Tatar":"tt",
"Telugu":"te",
"Thai":"th",
"Turkish":"tr",
"Turkmen":"tk",
"Ukrainian":"uk",
"Urdu":"ur",
"Uyghur":"ug",
"Uzbek":"uz",
"Vietnamese":"vi",
"Welsh":"cy",
"Xhosa":"xh",
"Yiddish":"yi",
"Yoruba":"yo",
"Zulu":"zu",
"Hebrew":"he",
"Chinese (Simplified)":"zh"
}

st.title("Language Translater")
in_lang=st.selectbox("input language",list(languages.keys()))

url = "https://text-translator2.p.rapidapi.com/translate"
text=st.text_area("enter text")

lang=st.selectbox("translate language",list(languages.keys()))
payload = {
"source_language":languages[in_lang],
"target_language":languages[lang],
"text": text
 }

headers = {
"content-type": "application/x-www-form-urlencoded",
"X-RapidAPI-Key": "e263672799msh5fee87fc8b00bd9p19807ejsn9f98bec00a24",
"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}
response = requests.post(url, data=payload, headers=headers)
got=response.json()
b=st.button("translate")
answer=dict(got)
answer=answer["data"]["translatedText"]
if b:
    st.title(answer)
    input_df=pd.read_csv("input_df.csv")
    input_update=pd.DataFrame({"Language": [in_lang], "text": [text],})
    df=pd.concat([input_df,input_update], ignore_index=True)
    df.to_csv("input_df.csv", index=False)

    output_df=pd.read_csv("output_df.csv")
    output_update=pd.DataFrame({"Language": [lang], "text": [answer],})
    new_df=pd.concat([output_df,output_update], ignore_index=True)
    new_df.to_csv("output_df.csv", index=False)
else:
    pass
d=st.button("data")
if d:
    st.dataframe(df)
    st.dataframe(new_df)
    
   
        

