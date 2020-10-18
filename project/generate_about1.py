# from save_page import generate_head, generate_body, generate_page
from save_page import generate_page, generate_head
from horoscope import times, advices, promises

parts = ["times", "advices", "promises"]
pic = '<img src="horoscope.jpg" width="100" height="100"/>'
link_main = '<a href="index.html">Back</a>'

def make_num_list(list):
	result = ""
	for item in list:
		result += "<ol>" + str(item) + "</ol>" 
	return result




def make_bullet_list(list):
	result = ""
	for item in list:
		result += "<li>" + str(item) + "</li>" 
	return result


def generate_body1(header, text):
    body = "<h1>" + header + "</h1>"
    body += pic
    body += text
    body += link_main
    # for p in paragraphs:
    #     body = body + f"<p>{p}</p>"
    return f"<body>{body}</body>"

def save_page1(output, title, header, text):
    fp = open(output, "w")
    page = generate_page(
        head=generate_head(title),
        body=generate_body1(header=header, text=text)
        )
    print(page, file=fp)
    fp.close()


times_list = make_bullet_list(times)
advices_list = make_bullet_list(advices)
promises_list =  make_bullet_list(promises)
parts_list = make_num_list(parts)



about = f"""
<ol>
    <li>{parts[0]}
        <ul>
        {times_list}
        </ul>
    </li>
    <li>{parts[1]}
        <ul>
        {advices_list}
        </ul>
    </li>
    <li>{
    parts[2]}
        <ul>
        {promises_list}
        </ul>
    </li>
</ol>"""
    


save_page1(
    output="about.html",
	title="How it works",
	header="What's this about",
	text=about
	)


