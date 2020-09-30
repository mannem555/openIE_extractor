from allennlp.predictors.predictor import Predictor
import allennlp_models.structured_prediction




def extract_helper(desc):
  data=desc.split("] ")
  arg_list={}
  for word in data:
      if word.find("[ARG")!=-1:
          temp=word.split(":")
    
          temp2=temp[0].split("[")
          arg=temp2[1]
          arg_list[arg]=temp[1].strip()
      elif word.find("[V:")!=-1:
          temp=word.split(":")
         
          arg_list["relation"]=temp[1].strip()
          
  return arg_list





def extract_triplets(sentence):
  predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/openie-model.2020.03.26.tar.gz")
  prediction=predictor.predict(
    sentence=sentence
  )
  
  triplets=[]
  for triplet in prediction['verbs']:
   
    print(triplet["description"])
    print("*"*50)
    desc=triplet["description"]
    triplets.append(extract_helper(desc))

  return triplets

text = "Shea butter is an excellent moisturizer for the face and the body. Its fat content is responsible for its emollient and humectant properties. It locks in the moisture in the skin and keeps it hydrated for long. Dehydrated and dry skin becomes rough and scaly. Certain areas of the body can even develop skin cracks due to dryness. Shea butter can nourish the skin with its fat content. It can also help to soften the skin on your hands and feet and make it supple. It penetrates the skin easily, without clogging the pores, and is effective for dry skin. Use shea butter to heal cracked heels, dry cuticles, and rough patches on your skin. You can also use it to simply moisturize your skin during the colder months."

print(extract_triplets(text))

