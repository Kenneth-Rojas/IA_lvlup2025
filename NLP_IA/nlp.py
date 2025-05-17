from textblob import TextBlob
from transformers import pipeline
npl_qa = pipeline("question-answering")
contexto = "Cada vez que abría su paraguas, dejaba de llover. Algunos pensaban que era magia; otros, solo coincidencia. Él, en cambio, se preguntaba si su fe en el paraguas era lo que realmente detenía la lluvia."
pregunta = "¿Qué idea principal transmite el texto?"

respuesta = npl_qa(question= pregunta, context= contexto)

print("Respuesta: ",respuesta)

nlp_generation = pipeline("text-generation")
txt = nlp_generation(contexto, max_length=100, do_sample= True)
print("Texto generado: ",txt[0]['generated_text'])

sentimiento = TextBlob(contexto).sentiment
print("Sentimiento: ",sentimiento)

nlp_resumen = resumen_model = pipeline("summarization")
resumen = nlp_resumen(contexto,max_length=50,do_sample=False)
print("Resumen: ",resumen[0]['summary_text'])


