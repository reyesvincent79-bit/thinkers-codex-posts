import json,sys
B={1:"The Science of Learning Your Inner Speech",2:"Learn To Think For Yourself",3:"The 14-Day Clarity Reset"}
def P(day,slot,hdr,q,attr,bodies,question,book,cta,cap1,cap2,tags):
    t={8:"0800",12:"1200",17:"1700",21:"2100"}[slot]; n=len(json.load(open('gen/_n.json'))) if False else 0
    s=[{"type":"cover","text":[q],"attr":attr}]
    s+= [{"type":"body","text":b} for b in bodies]
    s.append({"type":"question","text":[question]})
    s.append({"type":"body","text":[f"This is the thread behind the book *{B[book]}*.",cta[0]]})
    s.append({"type":"cta","text":cta[1],"button":"LINK IN BIO"})
    assert len(s)==10,(hdr,len(s))
    assert len(tags)<=5
    cap=f"{cap1}\n\n{cap2}\n\nFrom \"{B[book]}.\" Link in bio.\n\n"+" ".join("#"+x for x in tags)
    return {"id":f"d{day}_{t}","time":f"2026-11-{day:02d} {slot:02d}:00","header":hdr,"caption":cap,"slides":s}
posts=[]
A=posts.append
# ---- Nov 1
A(P(1,8,"On overthinking","“We suffer more often in imagination than in reality.”","SENECA",
 [["Most of what keeps you awake has not happened yet.","It is a rehearsal. A draft of a disaster, written by a nervous mind."],
  ["The mind is a brilliant storyteller.","Give it a blank space and it fills it with the worst case."],
  ["Notice the grammar of worry.","*What if. What if. What if.*","It never asks, *what is true right now?*"],
  ["Try a smaller question:","*What do I actually know?*","Separate the facts from the film your mind is playing."],
  ["Then give the voice a task.","Not *stop thinking.* That fails.","*Name the next small step.* Worry has nowhere to go once it has a job."],
  ["You cannot argue the future into behaving.","But you can talk to yourself like someone you trust today."]],
 "What is one worry you are rehearsing that you could turn into a single next step?",1,
 ["How to hear the loop, and how to redirect it.",["Quiet the loop.","*Keep the thinker.*"]],
 "The disaster you are rehearsing is not a forecast. It is a story.","Save this for the next time your mind spirals.",["overthinking","anxietyrelief","selftalk","mindset","innerspeech"]))
A(P(1,12,"On the examined life","“The unexamined life is not worth living.”","SOCRATES",
 [["He said it at his own trial, with his life on the line.","He did not mean *live perfectly.* He meant *live on purpose.*"],
  ["An unexamined life is not a bad one.","It is a *borrowed* one. Routine, expectation, other people’s timelines."],
  ["Examination is not self-punishment.","It is curiosity with a pen in your hand.","*Why do I want this? Who taught me to want it?*"],
  ["Start with one habit you never chose.","Your job. Your schedule. Your opinion of money.","Ask when you picked it, and whether you would pick it again."],
  ["Some answers will be uncomfortable.","That discomfort is information, not a verdict.","It points at the place where your own thinking begins."],
  ["You do not have to burn it all down.","You only have to *choose* what you keep."]],
 "Which part of your life have you never actually chosen?",2,
 ["Give yourself a method for choosing.",["Examine it.","*Then own it.*"]],
 "A life on autopilot is a life someone else planned.","Pick one thing today and ask: would I choose this again?",["thinkforyourself","socrates","criticalthinking","selfreflection","mindset"]))
A(P(1,17,"On wasted time","“It is not that we have a short time to live, but that we waste a lot of it.”","SENECA",
 [["He wrote this almost two thousand years ago.","He was describing a notification you have not received yet."],
  ["Time is rarely stolen in big pieces.","It leaks. Ten minutes here. A scroll there. A task that was never yours."],
  ["Most of us guard money carefully and hand out attention for free.","Attention is the thing you cannot earn back."],
  ["Clarity starts with an honest audit.","Where did yesterday actually go?","Not where you meant it to go."],
  ["Try this tonight:","List three things that took your time and gave nothing back.","Pick *one* to stop. Not all three."],
  ["A clear life is not a busier one.","It is one where your hours match your values."]],
 "If you could reclaim one hour a day, what would it go to?",3,
 ["Fourteen days of small, deliberate subtraction.",["Spend your hours.","*Do not leak them.*"]],
 "You are not short on time. You are short on a plan for it.","Try the three-item audit tonight.",["timemanagement","clarity","focus","seneca","mindset"]))
A(P(1,21,"On the mind’s weather","“All that we are is the result of what we have thought.”","THE BUDDHA (DHAMMAPADA)",
 [["The oldest self-help idea might also be the most practical.","*Thoughts become tone. Tone becomes habit. Habit becomes you.*"],
  ["Think about the last unkind thing you told yourself.","Now think about how many times you have repeated it.","That is not a thought anymore. It is a path."],
  ["Paths can be re-walked in a different direction.","Not by force. By *repetition.*","A new sentence, said often, becomes home."],
  ["Start by listening.","One day. No fixing.","Just notice what your inner voice says most."],
  ["You will hear patterns.","*Hurry. Not enough. Behind.*","You cannot change what you refuse to hear."],
  ["Then choose one replacement.","Short. Believable. Kind enough to repeat.","*That* is the work."]],
 "What does your inner voice say most often, and is it something you chose?",1,
 ["Exercises to hear it, name it, and rewrite it.",["Change the thought.","*Change the path.*"]],
 "Your thoughts are not just thoughts. They are a direction.","Tonight, listen without fixing anything.",["innerspeech","selftalk","mindfulness","mindset","growth"]))
# ---- Nov 2
A(P(2,8,"On self-knowledge","“Know thyself.”","DELPHIC MAXIM",
 [["Two words. Carved at the entrance to one of the ancient world’s great temples.","People traveled for days to read them."],
  ["They are harder than they sound.","Most of us know our résumé, our routines, our reactions.","Not the voice running underneath them."],
  ["Self-knowledge starts with listening.","What do you say to yourself when you fail?","When you succeed? When no one is around?"],
  ["Write down five sentences your inner voice says on repeat.","Then mark each one:","*Mine. Borrowed. Not sure.*"],
  ["The borrowed ones are the first to go.","They came from a critic, a parent, a bad season.","You can hand them back."],
  ["Knowing yourself is not a destination.","It is a daily conversation you finally start paying attention to."]],
 "What is the sentence you say to yourself most often, and who said it first?",1,
 ["A practical guide to the conversation you are already having.",["Know the voice.","*Then know yourself.*"]],
 "Before you change yourself, learn to hear yourself.","Try the five-sentence exercise today.",["knowthyself","innerspeech","selfawareness","selftalk","mindset"]))
A(P(2,12,"On trusting your mind","“Nothing is at last sacred but the integrity of your own mind.”","RALPH WALDO EMERSON",
 [["He wrote it in an essay called *Self-Reliance.*","It was not an invitation to be difficult. It was an invitation to be honest."],
  ["Integrity of mind means your thoughts and your actions agree.","No performing a belief you do not hold.","No holding a belief you never examined."],
  ["The pressure to conform rarely announces itself.","It sounds like *be realistic. Everyone does it. Don’t make waves.*"],
  ["Ask:","*Would I say this if no one could judge me?*","The honest answer is your starting point."],
  ["Independent thinking is a skill, not a personality.","You build it by reasoning out loud, by checking sources, by changing your mind when the evidence does."],
  ["The goal is not to stand alone.","It is to stand on ground you tested yourself."]],
 "Where are you performing a belief you do not actually hold?",2,
 ["A method for building a mind you can trust.",["Test it yourself.","*Then stand on it.*"]],
 "Your mind is the one thing you can’t outsource.","Name one belief you have never tested.",["thinkforyourself","emerson","selfreliance","independentthinking","mindset"]))
A(P(2,17,"On becoming","“First say to yourself what you would be; and then do what you have to do.”","EPICTETUS",
 [["It is a two-step instruction.","Most of us skip the first step and wonder why the second never lasts."],
  ["Deciding who you want to be is not a vision board.","It is a *sentence.* Short enough to say on a hard day."],
  ["Example:","*I am someone who finishes what I start.*","*I am someone who rests without guilt.*"],
  ["Then comes the unglamorous part.","One action that matches the sentence.","Today. Small enough to be boring."],
  ["Clarity is not a feeling you wait for.","It is the result of aligning what you say with what you do, over and over."],
  ["Fourteen days is long enough to feel the difference.","Short enough to start before you talk yourself out of it."]],
 "What is the one-sentence version of who you are choosing to be?",3,
 ["A 14-day structure for turning that sentence into a habit.",["Say it.","*Then do it, daily.*"]],
 "Identity is a sentence, repeated until it becomes action.","Write your one sentence on a sticky note.",["identity","clarity","stoicism","habits","mindset"]))
A(P(2,21,"On honest self-talk","“If it is not right, do not do it; if it is not true, do not say it.”","MARCUS AURELIUS",
 [["He wrote it in a private journal, to himself, never expecting anyone to read it.","That is the point. The first person you have to be honest with is you."],
  ["Most lies are small and internal.","*I’m fine. It doesn’t matter. I’ll do it tomorrow.*"],
  ["You say them so quickly that you almost believe them.","And the part of you that does not believe them goes quiet."],
  ["Honest self-talk is not harsh self-talk.","It is *accurate.*","*I’m tired* is true. *I’m worthless* is not."],
  ["Try a daily check:","*What did I tell myself today that was not true?*","One sentence. No judgment. Just the edit."],
  ["Integrity begins in the silent conversation.","Everything you say aloud grows from there."]],
 "What is one thing you tell yourself that you know is not quite true?",1,
 ["Learn to hear, check, and correct your inner voice.",["Be accurate.","*Not harsh.*"]],
 "The kindest self-talk is the most truthful.","Do the one-sentence check tonight.",["innerspeech","selftalk","honesty","stoicism","selfawareness"]))
# ---- Nov 3
A(P(3,8,"On self-mastery","“The first and best victory is to conquer self.”","PLATO",
 [["He wrote it in *Laws,* near the end of his life.","After a lifetime of arguing about everything else, this is what he came back to."],
  ["Conquering yourself is not about suppression.","It is about *noticing* the impulse before it acts."],
  ["Every impulse arrives with a sentence attached.","*Just one more. You deserve it. Later.*","The sentence is the handle."],
  ["Learn to catch the sentence.","You cannot stop the urge. You *can* answer it."],
  ["Answer once, calmly.","*I hear you. Not now.*","Over time the urge loses its argument."],
  ["Mastery is a quiet skill.","No one applauds the pause between the urge and the action.","That pause is where you live."]],
 "What sentence does your mind use to talk you out of what you meant to do?",1,
 ["How the inner voice drives behavior, and how to steer it.",["Catch the sentence.","*Keep the pause.*"]],
 "You do not win by force. You win by the pause.","Try answering one urge today with one calm sentence.",["selfmastery","innerspeech","discipline","plato","mindset"]))
A(P(3,12,"On hearing the other side","“He who knows only his own side of the case knows little of that.”","JOHN STUART MILL",
 [["From *On Liberty,* 1859.","A sentence that still describes most of the internet."],
  ["Thinking for yourself is not agreeing with yourself.","If you have only heard one side, you have not thought. You have recited."],
  ["Try the exercise in reverse.","Take a view you hold firmly.","Write the strongest case *against* it, as if you believed it."],
  ["If you cannot do it, that tells you something.","Not that you are wrong.","That you have not yet earned the confidence."],
  ["Independent thinking is not about being contrary.","It is about being *thorough.*"],
  ["Change your mind when the evidence does.","That is not weakness. That is what thinking is for."]],
 "What is the strongest argument against something you strongly believe?",2,
 ["Tools for reasoning, not just opinions.",["Hear the other side.","*Then decide.*"]],
 "If you can’t argue the other side, you don’t yet own your own.","Write the best case against one of your beliefs today.",["thinkforyourself","criticalthinking","openmind","johnstuartmill","mindset"]))
A(P(3,17,"On beginnings","“The beginning is the most important part of the work.”","PLATO",
 [["He was describing education.","But it is true of any change you have been putting off."],
  ["Beginnings are heavy because we attach the whole future to them.","*If I start, I have to finish. If I fail, it proves something.*"],
  ["Shrink the beginning until it is almost silly.","Two minutes. One page. One honest sentence.","Day one is not a performance."],
  ["The 14-day reset is built on this idea.","Each day asks for a small thing.","Small enough to do on a bad day."],
  ["Momentum is not motivation.","You do not wait to feel ready.","You do the small thing, and *then* you feel ready."],
  ["Fourteen small days will move you further than one heroic Monday."]],
 "What is the smallest possible version of the change you keep postponing?",3,
 ["Fourteen small, doable days, one idea each.",["Begin small.","*Begin today.*"]],
 "Do not wait for motivation. Make the first step small enough to take.","Do your two-minute version now.",["clarity","habits","beginnings","selfimprovement","mindset"]))
A(P(3,21,"On quiet desperation","“The mass of men lead lives of quiet desperation.”","HENRY DAVID THOREAU",
 [["From *Walden.* Maybe the most uncomfortable line in American literature.","Not loud misery. Quiet. Almost polite."],
  ["You can be productive and still feel hollow.","Busy and unfulfilled.","Surrounded and unheard, even by yourself."],
  ["Quiet desperation rarely has a cause.","It has a *drift.* Years of small decisions nobody questioned."],
  ["The first step is not a dramatic exit.","It is a question asked sincerely.","*Is this what I want, or just what I got used to?*"],
  ["You may not like the answer.","But an honest answer is the first thing in years that has been yours."],
  ["Thoreau did not tell everyone to leave town.","He told them to *live deliberately.*"]],
 "If nothing changed, what would the next five years of your life look like?",2,
 ["A process for questioning the script and writing your own.",["Live deliberately.","*Think for yourself.*"]],
 "Drift is not destiny. It is a pattern you can question.","Ask yourself the question once, honestly, tonight.",["thoreau","thinkforyourself","livingdeliberately","selfreflection","mindset"]))
# ---- Nov 4
A(P(4,8,"On the thinker","“I think, therefore I am.”","RENÉ DESCARTES",
 [["He reached it by doubting everything he could doubt.","What was left was the act of doubting itself: *a mind at work.*"],
  ["You are not your reaction. You are not your mood.","You are the one who *notices* them."],
  ["That noticing self is the most overlooked part of you.","It is quiet. It does not shout like the critic does."],
  ["Practice finding it.","Pause once an hour.","Ask: *What is being said in my head right now?*"],
  ["The moment you ask, you are no longer inside the sentence.","You are the one hearing it."],
  ["That distance is the beginning of choice."]],
 "Who is the one listening when you hear your own thoughts?",1,
 ["Meet the part of you that listens.",["Be the listener.","*Then lead the voice.*"]],
 "You are the one who hears the thought, not the thought itself.","Pause once an hour today and just listen.",["innerspeech","descartes","mindfulness","selfawareness","mindset"]))
A(P(4,12,"On belonging to yourself","“The greatest thing in the world is to know how to belong to oneself.”","MICHEL DE MONTAIGNE",
 [["He retired to a tower in his estate and wrote essays about himself.","Not out of vanity. Out of curiosity about how a person actually thinks."],
  ["To belong to yourself means your day, your time, and your mind are, at least partly, yours.","Not on loan to every request."],
  ["It does not mean isolation.","It means having a room inside you that others can visit but not rearrange."],
  ["Build it with small refusals.","One call you do not take. One opinion you do not adopt.","One hour that is not for anyone else."],
  ["It will feel selfish at first.","It is the opposite.","People who belong to themselves are the ones with something to give."],
  ["Start with an hour. Protect it like an appointment."]],
 "What is one hour this week that could belong entirely to you?",2,
 ["How to reclaim your own thinking, one decision at a time.",["Belong to yourself.","*Think for yourself.*"]],
 "An inner room of your own is not selfish. It is where your thinking lives.","Block one hour this week and protect it.",["montaigne","thinkforyourself","selfreliance","independentthinking","mindset"]))
A(P(4,17,"On purpose","“He who has a why to live can bear almost any how.”","FRIEDRICH NIETZSCHE",
 [["Viktor Frankl later made the line famous.","Nietzsche wrote it first."],
  ["Clutter is not only physical.","It is the pile of things you are doing without knowing why."],
  ["When you cannot say why, everything feels equally urgent.","And exhausting."],
  ["A *why* is a filter.","It lets you say no without guilt.","It turns a long list into a short one."],
  ["Write yours in one sentence.","*I want my days to ____ so that ____.*","It does not have to be grand. It has to be true."],
  ["Then look at your week.","What serves the sentence, and what is only noise?"]],
 "If you had to explain your week in one sentence, what would it say you live for?",3,
 ["A clear why makes the rest of the reset easy.",["Find the why.","*Clear the rest.*"]],
 "A clear why makes most decisions for you.","Write your one-sentence why before you sleep.",["purpose","clarity","nietzsche","focus","mindset"]))
A(P(4,21,"On daily reset","“Begin at once to live, and count each separate day as a separate life.”","SENECA",
 [["It was advice to a friend, written near the end of his own life.","He had stopped waiting for a better season to begin."],
  ["The day is a smaller unit than we treat it as.","One day is enough time to change direction."],
  ["A day does not need to be perfect.","It needs to be *finished.* Closed on purpose."],
  ["Try a nightly reset:","*What went well. What I will drop. One thing for tomorrow.*","Three lines. Under two minutes."],
  ["Over fourteen nights, something shifts.","The days stop piling up.","They start to feel like *yours.*"],
  ["You do not need a new year to start over.","You need a new evening."]],
 "What would you want tomorrow’s version of today to look like?",3,
 ["Two weeks of small nightly resets, one clear mind.",["Close the day.","*Begin again.*"]],
 "You get to start over every single night.","Try the three-line reset tonight.",["dailyreset","seneca","clarity","stoicism","mindset"]))
json.dump(posts,open(sys.argv[1],"w"),indent=1,ensure_ascii=False); print(len(posts))
