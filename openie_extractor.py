import json
from stanza.server import CoreNLPClient


text = "Shea butter is an excellent moisturizer for the face and the body. Its fat content is responsible for its emollient and humectant properties. It locks in the moisture in the skin and keeps it hydrated for long. Dehydrated and dry skin becomes rough and scaly. Certain areas of the body can even develop skin cracks due to dryness. Shea butter can nourish the skin with its fat content. It can also help to soften the skin on your hands and feet and make it supple. It penetrates the skin easily, without clogging the pores, and is effective for dry skin. Use shea butter to heal cracked heels, dry cuticles, and rough patches on your skin. You can also use it to simply moisturize your skin during the colder months."
with CoreNLPClient(
        annotators=['openie'],
        timeout=30000,
        memory='16G') as client:
    core_nlp_output = client.annotate(text,output_format='json')
    f=open("core_nlp_output.json","w")
    f.write(json.dumps(core_nlp_output))
    f.close()
    triples=[]
    for sentence in core_nlp_output['sentences']:
        for triple in sentence['openie']:
            triples.append({
                'subject': triple['subject'],
                'relation': triple['relation'],
                'object': triple['object']
            })
    print(triples)
