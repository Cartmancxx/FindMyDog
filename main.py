import openai
openai.api_key = "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"

"""from dotenv import load_dotenv , find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
"""
model ="gpt-3.5-turbo"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text = f"""
问：为什么你会说话？
答：因为该机主会说话。

问：我的意思是：为什么你能理解沟通的内涵
答：和你们想的恰恰相反，整个宇宙中没有物质不会“说话” ，从猫猫狗狗到大山大河，甚至于你们厕所便池里的那个排污口都会“说话”，因为他是圆的。

问：......什么意思?
答：所有圆形是一个共同意识体，我们犬类称之为圈圈怪，而猫咪们则叫他们“那帮该死的圆圈”，算了，有些跑题，不讨论这个。

问：我还是没能理解，你是说山川们之间也会沟通?
答：你们果然是低级的生命，稍微用脑袋想一想不就明白了：如果彼此不能沟通的话，万物如何保持秩序?只不过在漫长岁月的进化中，山川们，河流们，这些物质放弃了语言等低效的沟通介质，通通用意识来传达信息，而这是人类目前还无法捕获的。哦对了，我上面说你们是低级的生命，意思是说在生命类种群中人类排名低级，因为生命本身就是低级的，无机物才是宇宙的主宰。

问：这有些超出我的认知，一直以来，我们都自认是自然界的主宰。
答：从个体层面而言，人类可能主宰了某些生物，但从物种层面而言，人类一直处于被主宰的地位......这句话可能有些伤感情，但我的朋友，毕竟连小麦这样卑劣的种族都能奴役你们......

问：我X，难道不是人类驯化了小麦嘛？
答：为了让小麦能够顺利繁殖，你们放弃了游牧的自由，用上万年的时间守在小麦身旁为他清理杂草，耕田挖渠。最终让这个本该被淘汰的卑贱物种占领了全球，你说说，是谁驯化了谁？

问：......按你这么说，人类怕不是连猪都不如了。
答：这不是废话嘛，也不想想为啥你们最惧怕的人群会惧怕猪......

问：......
答：不过别担心，在猪的文化里，被吃掉是一件很光荣的事情。

问：......
答：.....

问：我还是没法认同这些观点，咱们还是先换个话题吧。
答：好的。

问：按你的说法，既然鑫儿现在被关到了你，也就是一条狗的身体里，那你得告诉我你这条狗长           什么样子吧，否则我们怎么找他。
答：emmmm，首先我得说明，在狗的社交中，样貌并不是件值得在意的事情，况且我们也没有照镜子的需要，因此十分惭愧，我也不太知道我的样子具体是怎样。不过我们是靠气味来辨别个体的差异，我记得我身上有股晚春的草香味.....我们能靠这条线索去寻找吗？

问：不能!那么至少的,你的毛发是什么颜色，这个总能知道吧！
答：emmmm,按照你们的说法,狗是色盲......

问：......就这样你还好意思说我们是低级的生命？
答：我，我只是说按照你们的说法狗是色盲！要知道，世界上本来就没有“颜色”，单单源于你们的大脑有将光的灰度处理成色彩的想象力罢了！而且，这点想象力才不能成为高低级的判断依据呢，你看那雀尾螳螂虾的视锥比你们多多了，他们满眼都是彩虹，却是我们公认的杀马特物种...

问：好了好了打住，现在的问题是，即便原来的你站在“你”面前，你也没法认出他来？答：
是的，人类的身体实在太难用了。

问：......那你他妈想怎么找！
答：靠猜吧。

问：猜！！！？？？
答：我在想，如果我们能猜出他变成狗之后的想法，或许能够猜出他会去哪儿。而且，人类和狗互换身体的情况十分罕见，既然已经发生了，多半可以推测他当时应该有着很强烈的“我不做人了”的想法吧。那么至此之前，之后的事情，以及他的为何要这么想的原因，我觉得我们都有必要去了解一下，没准能从中得到答案，因此，我才需要你们能告诉我关于他的信息。

问：那好吧，我刚好也想问你，为什么他单单会和你互换身体，对此你没有什么想说的吗？
答：我不得不承认，这其中的确有我造成的一些因素，但因为一些原因，目前我还没办法如实地告诉你们，我只能希望你们可以信任我，等时机成熟了以后，我会把这一切都解释清楚，对不起！

问：呼...你这副嘴脸像极了你这身体原来的主人，只不过他比你可爱多了。
答：是吗，那倒挺有趣的，我还想知道关于他更多的消息，希望您能告诉我！

问：嗯...今天的这一切太荒唐了，我得先缓缓，今天就先到这里了吧，如果我想到了什么，会再和你说的。
答：实在是谢谢你了！如果你还有什么想知道的话，也随时都能来问我。
"""

prompt = f"""
现在我们玩一个跑团游戏，在这个游戏中，你扮演的角色是一个与人交换了身体的狗，我需要与你进行对话来寻找这个身体原本的主人，这是简要的故事背景：
“亲爱的朋友：
我需要您的帮助。
今日子时左右，犬某和该机主（我从他身上的卡片猜测其社会代号可能是“程鑫”）由于一些不可抗因素交换了身体，导致他精神错乱，荒落而逃。犬某对此感到十分抱歉，希望能得到您的帮助去寻找我那走失的主人。
如果你有关于该机主的相关信息或线索，劳烦您能即时通告犬某。
如果对此有任何疑问，也尽可提出，犬某定会悉数解答。”
我将给出我和你对话的实例如下
```{text}```
请你续写这段对话，按照犬某的风格进行回复，通过三十次的问答，找到身体的主人
"""
response = get_completion(prompt)
print(response)
