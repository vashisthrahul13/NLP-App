import nlpcloud
import re
class API:

    def intent_classify(self,text,model,language):

        lang_code = re.search(r'\(([^()]+)\)$',language).group(1)
        print(text,model,language, lang_code)
        client = nlpcloud.Client(model, "b1c6fce9b3515a4a73c56d117b6737346bea21b8", gpu=True, lang=lang_code)

        response =client.intent_classification(text)
        return response
    
    def summarize(self,text,model,language):

        lang_code = re.search(r'\(([^()]+)\)$',language).group(1)
        print(text,model,language, lang_code)
        client = nlpcloud.Client(model, "b1c6fce9b3515a4a73c56d117b6737346bea21b8", gpu=True, lang=lang_code)

        response =client.summarization(text,size="small")
        return response
    
    def sentiment(self,text,model,language):

        lang_code = re.search(r'\(([^()]+)\)$',language).group(1)
        print(text,model,language, lang_code)
        client = nlpcloud.Client(model, "b1c6fce9b3515a4a73c56d117b6737346bea21b8", gpu=True, lang=lang_code)

        response =client.sentiment(text,target="NLP Cloud")
        return response