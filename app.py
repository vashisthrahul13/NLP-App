from tkinter import *
from db_manage import Database
from tkinter import messagebox
import re
from api_call import API

class MyApp:

    def __init__(self):

        self.dbo = Database()
        self.apio = API()
        self.root = Tk()        #creating object of Tk class

        self.root.title('MyApp')
        self.root.iconbitmap('resources/favicon.ico')   #icon for app ;only ico format allowed
        self.root.geometry('500x600')   #sets the default size of window
        self.root.configure(background='#34495E')

        self.login_gui()

        self.root.mainloop()    #holds the GUI on screen


    # main login page
    def login_gui(self):
        
        self.clear()

        main_heading = Label(self.root, text = 'NLP App' , background= '#34495E' , foreground= 'white')
        main_heading.pack(pady=(30,30))
        main_heading.configure(font= ('verdana',24, 'bold'))
        
        label1= Label(self.root, text= 'Enter Email')
        label1.pack(pady = (10,10))
        
        self.email_input = Entry(self.root,width = 50)
        self.email_input.pack(pady= (10,10),ipady= 4)
    
        label2= Label(self.root,text= "Enter password")
        label2.pack(pady = (10,10))
        self.password_input = Entry(self.root,width = 50,show= '*')
        self.password_input.pack(pady=(10,10), ipady = 4)

        login_btn = Button(self.root,text='Login',width=15,height =2 ,command = self.perform_login)
        login_btn.pack(pady = (15,15))

        label3 = Label(self.root,text= 'Not a member?')
        label3.pack(pady = (15,15))
        redirect_btn = Button(self.root, text= 'Register Now',command = self.register_gui)
        redirect_btn.pack(pady = (10,10))


    #Function to perform login
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.check_user(email,password)

        if response == 0:
            messagebox.showerror('Error', 'User not found')
        if response==1:
            messagebox.showerror('Success', 'Congratulations! Login successful')
            self.nlp_gui()
        if response==2:
            messagebox.showerror('Error', 'Incorrect Email/password')


    #GUI to perform registration
    def register_gui(self):
        self.clear()
        
        main_heading = Label(self.root, text = 'Register' , background= '#34495E' , foreground= 'white')
        main_heading.pack(pady=(30,30))
        main_heading.configure(font= ('verdana',24, 'bold'))
        
        label0= Label(self.root, text= 'Enter name')
        label0.pack(pady = (10,10))
        self.name_input = Entry(self.root,width = 50)
        self.name_input.pack(pady= (10,10),ipady= 4)
        #print(type(self.name_input)) -> class tkinter.Entry

        label1= Label(self.root, text= 'Enter Email')
        label1.pack(pady = (10,10))
        self.email_input = Entry(self.root,width = 50)
        self.email_input.pack(pady= (10,10),ipady= 4)
    
        label2= Label(self.root,text= "Enter password")
        label2.pack(pady = (10,10))
        self.password = Entry(self.root,width = 50,show= '*')
        self.password.pack(pady=(10,10), ipady = 4)

        register_btn = Button(self.root,text='Register',width=15,height =2 , command = self.perform_registration)
        register_btn.pack(pady = (15,15))

        label3 = Label(self.root,text= 'Already a member?')
        label3.pack(pady = (15,15))
        redirect_btn = Button(self.root, text= 'Login Now',command = self.login_gui)
        redirect_btn.pack(pady = (10,10))


    #function to verify details and do registration
    def perform_registration(self):
        name= self.name_input.get()
        email = self.email_input.get()
        password = self.password.get()

        if name=='' or email=='' or password=='':
            messagebox.showerror('Error','One of the fields is empty')
        elif self.check_valid_email(email)==False:
            messagebox.showerror('Error',"Invalid format of email")
        else:
            response = self.dbo.add_user(name,email,password)
            if response:
                messagebox.showerror('Success','Registration Successful. Login now')
                self.login_gui()
            else:
                messagebox.showerror('Error','Email already exist')


    # Main gui after login successful
    def nlp_gui(self):
        self.clear()

        main_heading = Label(self.root,text= 'NLP App',background= '#34495E' , foreground= 'white')
        main_heading.pack(pady=(30,30))
        main_heading.configure(font= ('verdana',24, 'bold'))

        intent_classify_btn = Button(self.root, text = 'Intent Classification', width = 30, height= 3 ,command = self.intent_classify_gui)
        intent_classify_btn.pack(pady = (15,15))

        summarization_btn = Button(self.root, text = 'Summarization' , width = 30 , height = 3,command= self.summarization_gui)
        summarization_btn.pack(pady = (15,15))

        sentiment_analysis_btn = Button(self.root, text= 'Sentiment Analysis', width = 30 , height =3,command= self.sentiment_gui)
        sentiment_analysis_btn.pack(pady= (15,15))


    def intent_classify_gui(self):
        self.clear()
        desc = """Intent classification (also known as intent detection, or intent recognition) is about retrieving the intent from a piece of text. This is especially useful in a discussion (i.e. chatbots and conversational AI), in order to understand what a person wants to achieve. In a conversation between an AI and a human, it can be very useful to understand what the person is truly looking for or asking for."""

        main_label = Label(self.root, text = 'Intent Classification',background= '#34495E', foreground= 'white')
        main_label.pack(pady = (30,30))
        main_label.configure(font= ('verdana',24,'bold'))

        label0 = Label(self.root, text = desc,wraplength= 500 ,anchor='center',justify='left',background= '#34495E', foreground= 'white')
        label0.pack(pady= (15,15))
        label0.configure(font=('verdana',15))

        # Define options for the dropdown
        model_options = self.input_options()[0]
        lang_options = self.input_options()[1]

        # Create a StringVar to hold the selected value
        self.selected_model = StringVar()
        self.selected_model.set(model_options[0])  # Set the default value
        self.selected_lang= StringVar()
        self.selected_lang.set(lang_options[0])

        # Create a frame to hold the dropdown and button side by side
        frame = Frame(self.root)
        frame.pack(pady=20)

        # Create the dropdown menu
        dropdown1 = OptionMenu(frame, self.selected_model, *model_options)
        dropdown1.pack(side="left", padx=10)

        dropdown2 = OptionMenu(frame, self.selected_lang , *lang_options)
        dropdown2.pack(side="left", padx=10)

        button = Button(frame, text="Analyse", command=self.do_intent_classification)
        button.pack(pady= (10,10))

        self.intent_input = Text(self.root,height = 5,width = 50, wrap='word') #Text allows for multiline input -> Entry allows for single line input
        self.intent_input.pack(pady = (15,15))

        goback_btn = Button(self.root, text='Go Back', command=self.nlp_gui)
        goback_btn.pack(pady=(10, 10))


    def do_intent_classification(self):
        input_text = self.intent_input.get("1.0", "end-1c")  # "1.0" is the start, "end-1c" is the end
        input_model = self.selected_model.get()
        input_lang = self.selected_lang.get()
        
        response = self.apio.intent_classify(input_text,input_model,input_lang)

        label0 = Label(self.root, text=response)
        label0.pack(pady= (15,15))


    def summarization_gui(self):
        self.clear()
        desc = """Text summarization simply is the process of summarizing a block of text in order to make it shorter while maintaining the general idea being conveyed."""

        main_label = Label(self.root, text = 'Summarization',background= '#34495E', foreground= 'white')
        main_label.pack(pady = (30,30))
        main_label.configure(font= ('verdana',24,'bold'))

        label0 = Label(self.root, text = desc,wraplength= 500 ,anchor='center',justify='left',background= '#34495E', foreground= 'white')
        label0.pack(pady= (15,15))
        label0.configure(font=('verdana',15))

        # Define options for the dropdown
        model_options = self.input_options()[0]
        lang_options = self.input_options()[1]

        # Create a StringVar to hold the selected value
        self.selected_model = StringVar()
        self.selected_model.set(model_options[0])  # Set the default value
        self.selected_lang= StringVar()
        self.selected_lang.set(lang_options[0])

        # Create a frame to hold the dropdown and button side by side
        frame = Frame(self.root)
        frame.pack(pady=20)

        # Create the dropdown menu
        dropdown1 = OptionMenu(frame, self.selected_model, *model_options)
        dropdown1.pack(side="left", padx=10)

        dropdown2 = OptionMenu(frame, self.selected_lang , *lang_options)
        dropdown2.pack(side="left", padx=10)

        button = Button(frame, text="Analyse", command=self.do_summarization)
        button.pack(pady= (10,10))

        self.summarize_input = Text(self.root,height = 5,width = 50, wrap='word')
        self.summarize_input.pack(pady = (15,15))

        goback_btn = Button(self.root, text='Go Back', command=self.nlp_gui)
        goback_btn.pack(pady=(10, 10))

    def do_summarization(self):
        input_text = self.summarize_input.get("1.0", "end-1c")  # "1.0" is the start, "end-1c" is the end
        input_model = self.selected_model.get()
        input_lang = self.selected_lang.get()
        
        response = self.apio.summarize(input_text,input_model,input_lang)

        label0 = Label(self.root, text=response)
        label0.pack(pady= (15,15))

    def sentiment_gui(self):
        self.clear()
        desc = """Sentiment analysis is the process of extracting a general sentiment from a block of text. Basically it's about determining whether the text is positive or negative. This can be used to analyse user opinion,product reviews,movie reviews etc"""

        main_label = Label(self.root, text = 'Sentiment Analysis',background= '#34495E', foreground= 'white')
        main_label.pack(pady = (30,30))
        main_label.configure(font= ('verdana',24,'bold'))

        label0 = Label(self.root, text = desc,wraplength= 500 ,anchor='center',justify='left',background= '#34495E', foreground= 'white')
        label0.pack(pady= (15,15))
        label0.configure(font=('verdana',15))

        # Define options for the dropdown
        model_options = self.input_options()[0]
        lang_options = self.input_options()[1]

        # Create a StringVar to hold the selected value
        self.selected_model = StringVar()
        self.selected_model.set(model_options[0])  # Set the default value
        self.selected_lang= StringVar()
        self.selected_lang.set(lang_options[0])

        # Create a frame to hold the dropdown and button side by side
        frame = Frame(self.root)
        frame.pack(pady=20)

        # Create the dropdown menu
        dropdown1 = OptionMenu(frame, self.selected_model, *model_options)
        dropdown1.pack(side="left", padx=10)

        dropdown2 = OptionMenu(frame, self.selected_lang , *lang_options)
        dropdown2.pack(side="left", padx=10)

        button = Button(frame, text="Analyse", command=self.do_sentiment)
        button.pack(pady= (10,10))

        self.sentiment_input = Text(self.root,height = 5,width = 50, wrap='word')
        self.sentiment_input.pack(pady = (15,15))

        goback_btn = Button(self.root, text='Go Back', command=self.nlp_gui)
        goback_btn.pack(pady=(10, 10))


    def do_sentiment(self):
        input_text = self.sentiment_input.get()
        input_model = self.selected_model.get()
        input_lang = self.selected_lang.get()
        
        response = self.apio.sentiment(input_text,input_model,input_lang)

        label0 = Label(self.root, text=response)
        label0.pack(pady= (15,15))

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def check_valid_email(self,email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Use re.match to check if the email matches the pattern
        return re.match(email_regex, email) is not None
    
    def input_options(self):
        model_options = ["finetuned-llama-3-70b","llama-3-1-405b", "chatdolphin","dolphin-yi-34b","dolphin-mixtral-8x7b"]
        lang_options = ['English (eng_Latn)', 'Acehnese (Arabic script) (ace_Arab)', 'Acehnese (Latin script) (ace_Latn)', 'Afrikaans (afr_Latn)', 'Akan (aka_Latn)', 'Amharic (amh_Ethi)', 'Armenian (hye_Armn)', 'Assamese (asm_Beng)', 'Asturian (ast_Latn)', 'Awadhi (awa_Deva)', 'Ayacucho Quechua (quy_Latn)', 'Balinese (ban_Latn)', 'Bambara (bam_Latn)', 'Banjar (Arabic script) (bjn_Arab)', 'Banjar (Latin script) (bjn_Latn)', 'Bashkir (bak_Cyrl)', 'Basque (eus_Latn)', 'Belarusian (bel_Cyrl)', 'Bemba (bem_Latn)', 'Bengali (ben_Beng)', 'Bhojpuri (bho_Deva)', 'Bosnian (bos_Latn)', 'Buginese (bug_Latn)', 'Bulgarian (bul_Cyrl)', 'Burmese (mya_Mymr)', 'Catalan (cat_Latn)', 'Cebuano (ceb_Latn)', 'Central Atlas Tamazight (tzm_Tfng)', 'Central Aymara (ayr_Latn)', 'Central Kanuri (Arabic script) (knc_Arab)', 'Central Kanuri (Latin script) (knc_Latn)', 'Central Kurdish (ckb_Arab)', 'Chhattisgarhi (hne_Deva)', 'Chinese (Simplified) (zho_Hans)', 'Chinese (Traditional) (zho_Hant)', 'Chokwe (cjk_Latn)', 'Crimean Tatar (crh_Latn)', 'Croatian (hrv_Latn)', 'Czech (ces_Latn)', 'Danish (dan_Latn)', 'Dari (prs_Arab)', 'Dutch (nld_Latn)', 'Dyula (dyu_Latn)', 'Dzongkha (dzo_Tibt)', 'Eastern Panjabi (pan_Guru)', 'Eastern Yiddish (ydd_Hebr)', 'Egyptian Arabic (arz_Arab)', 'English (eng_Latn)', 'Esperanto (epo_Latn)', 'Estonian (est_Latn)', 'Ewe (ewe_Latn)', 'Faroese (fao_Latn)', 'Fijian (fij_Latn)', 'Finnish (fin_Latn)', 'Fon (fon_Latn)', 'French (fra_Latn)', 'Friulian (fur_Latn)', 'Galician (glg_Latn)', 'Ganda (lug_Latn)', 'Georgian (kat_Geor)', 'German (deu_Latn)', 'Greek (ell_Grek)', 'Guarani (grn_Latn)', 'Gujarati (guj_Gujr)', 'Haitian Creole (hat_Latn)', 'Halh Mongolian (khk_Cyrl)', 'Hausa (hau_Latn)', 'Hebrew (heb_Hebr)', 'Hindi (hin_Deva)', 'Hungarian (hun_Latn)', 'Icelandic (isl_Latn)', 'Igbo (ibo_Latn)', 'Ilocano (ilo_Latn)', 'Indonesian (ind_Latn)', 'Irish (gle_Latn)', 'Italian (ita_Latn)', 'Japanese (jpn_Jpan)', 'Javanese (jav_Latn)', 'Jingpho (kac_Latn)', 'Kabiyè (kbp_Latn)', 'Kabuverdianu (kea_Latn)', 'Kabyle (kab_Latn)', 'Kamba (kam_Latn)', 'Kannada (kan_Knda)', 'Kashmiri (Arabic script) (kas_Arab)', 'Kashmiri (Devanagari script) (kas_Deva)', 'Kazakh (kaz_Cyrl)', 'Khmer (khm_Khmr)', 'Kikongo (kon_Latn)', 'Kikuyu (kik_Latn)', 'Kimbundu (kmb_Latn)', 'Kinyarwanda (kin_Latn)', 'Korean (kor_Hang)', 'Kyrgyz (kir_Cyrl)', 'Lao (lao_Laoo)', 'Latgalian (ltg_Latn)', 'Ligurian (lij_Latn)', 'Limburgish (lim_Latn)', 'Lingala (lin_Latn)', 'Lithuanian (lit_Latn)', 'Lombard (lmo_Latn)', 'Luba-Kasai (lua_Latn)', 'Luo (luo_Latn)', 'Luxembourgish (ltz_Latn)', 'Macedonian (mkd_Cyrl)', 'Magahi (mag_Deva)', 'Maithili (mai_Deva)', 'Malayalam (mal_Mlym)', 'Maltese (mlt_Latn)', 'Maori (mri_Latn)', 'Marathi (mar_Deva)', 'Meitei (Bengali script) (mni_Beng)', 'Mesopotamian Arabic (acm_Arab)', 'Minangkabau (Arabic script) (min_Arab)', 'Minangkabau (Latin script) (min_Latn)', 'Mizo (lus_Latn)', 'Modern Standard Arabic (Romanized) (arb_Latn)', 'Modern Standard Arabic (arb_Arab)', 'Moroccan Arabic (ary_Arab)', 'Mossi (mos_Latn)', 'Najdi Arabic (ars_Arab)', 'Nepali (npi_Deva)', 'Nigerian Fulfulde (fuv_Latn)', 'North Azerbaijani (azj_Latn)', 'North Levantine Arabic (apc_Arab)', 'Northern Kurdish (kmr_Latn)', 'Northern Sotho (nso_Latn)', 'Northern Uzbek (uzn_Latn)', 'Norwegian Bokmål (nob_Latn)', 'Norwegian Nynorsk (nno_Latn)', 'Nuer (nus_Latn)', 'Nyanja (nya_Latn)', 'Occitan (oci_Latn)', 'Odia (ory_Orya)', 'Pangasinan (pag_Latn)', 'Papiamento (pap_Latn)', 'Plateau Malagasy (plt_Latn)', 'Polish (pol_Latn)', 'Portuguese (por_Latn)', 'Romanian (ron_Latn)', 'Rundi (run_Latn)', 'Russian (rus_Cyrl)', 'Samoan (smo_Latn)', 'Sango (sag_Latn)', 'Sanskrit (san_Deva)', 'Santali (sat_Olck)', 'Sardinian (srd_Latn)', 'Scottish Gaelic (gla_Latn)', 'Serbian (srp_Cyrl)', 'Shan (shn_Mymr)', 'Shona (sna_Latn)', 'Sicilian (scn_Latn)', 'Silesian (szl_Latn)', 'Sindhi (snd_Arab)', 'Sinhala (sin_Sinh)', 'Slovak (slk_Latn)', 'Slovenian (slv_Latn)', 'Somali (som_Latn)', 'South Azerbaijani (azb_Arab)', 'South Levantine Arabic (ajp_Arab)', 'Southern Pashto (pbt_Arab)', 'Southern Sotho (sot_Latn)', 'Southwestern Dinka (dik_Latn)', 'Spanish (spa_Latn)', 'Standard Latvian (lvs_Latn)', 'Standard Malay (zsm_Latn)', 'Standard Tibetan (bod_Tibt)', 'Sundanese (sun_Latn)', 'Swahili (swh_Latn)', 'Swati (ssw_Latn)', 'Swedish (swe_Latn)', 'Tagalog (tgl_Latn)', 'Tajik (tgk_Cyrl)', 'Tamasheq (Latin script) (taq_Latn)', 'Tamasheq (Tifinagh script) (taq_Tfng)', 'Tamil (tam_Taml)', 'Tatar (tat_Cyrl)', 'Ta\'izzi-Adeni Arabic (acq_Arab)', 'Telugu (tel_Telu)', 'Thai (tha_Thai)', 'Tigrinya (tir_Ethi)', 'Tok Pisin (tpi_Latn)', 'Tosk Albanian (als_Latn)', 'Tsonga (tso_Latn)', 'Tswana (tsn_Latn)', 'Tumbuka (tum_Latn)', 'Tunisian Arabic (aeb_Arab)', 'Turkish (tur_Latn)', 'Turkmen (tuk_Latn)', 'Twi (twi_Latn)', 'Ukrainian (ukr_Cyrl)', 'Umbundu (umb_Latn)', 'Urdu (urd_Arab)', 'Uyghur (uig_Arab)', 'Venetian (vec_Latn)', 'Vietnamese (vie_Latn)', 'Waray (war_Latn)', 'Welsh (cym_Latn)', 'West Central Oromo (gaz_Latn)', 'Western Persian (pes_Arab)', 'Wolof (wol_Latn)', 'Xhosa (xho_Latn)', 'Yoruba (yor_Latn)', 'Yue Chinese (yue_Hant)', 'Zulu (zul_Latn)']

        return [model_options,lang_options]
app = MyApp()
app.update_idletasks()

