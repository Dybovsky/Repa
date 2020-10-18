import random

times = ["in the morning", "in the afternoon", "in the evening", "at night", "after dinner", "before bedtime"]
advices = ["expect", "beware", "be open to"]
promises = ["guests from the forgotten past "," meetings with old friends ",
            "unexpected holiday", "pleasant changes"]


def generate_prophecies(total_num=3, num_sentences=4):
    prophecies = []

    
    for i in range(total_num):

        forecast = ""

        for j in range(num_sentences):

            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f"{t.title()} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
            j = j + 1

        prophecies.append(forecast)
        i = i + 1

    return prophecies





def generate_body(header, paragraphs):
    body = "<h1>" + header + "</h1>"
    par = paragraphs()
    for p in par:
        body +="<p>"+p+"</p>"
    return "<body>" + body + "</body>"




generate_prophecies()
generate_body(header="Гороскоп на 2018-11-12", paragraphs=generate_prophecies)