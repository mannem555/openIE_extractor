from openie import StanfordOpenIE
import json

with StanfordOpenIE() as client:
    # text = "Shea butter is an excellent moisturizer for the face and the body. Its fat content is responsible for its emollient and humectant properties. It locks in the moisture in the skin and keeps it hydrated for long. Dehydrated and dry skin becomes rough and scaly. Certain areas of the body can even develop skin cracks due to dryness. Shea butter can nourish the skin with its fat content. It can also help to soften the skin on your hands and feet and make it supple. It penetrates the skin easily, without clogging the pores, and is effective for dry skin. Use shea butter to heal cracked heels, dry cuticles, and rough patches on your skin. You can also use it to simply moisturize your skin during the colder months."
    # print('Text: %s.' % text)
    # for triple in client.annotate(text):
    #     print('|-', triple)

    with open("data.json") as json_data:
        data=json.load(json_data)
        for cat,text in zip(data.keys(),data.values()):
            print(cat)
            print(text)
            for triple in client.annotate(text):
                print('|-', triple)
